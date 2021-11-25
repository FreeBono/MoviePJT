
import numpy as np
import pandas as pd
from IPython.display import set_matplotlib_formats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from ast import literal_eval
import warnings
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json, requests
from django.contrib.auth import SESSION_KEY
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import Movie, UpcomingMovie
from .serializers import MovieSerializer
from django.http import JsonResponse


plt.show()
set_matplotlib_formats('retina')
mpl.rc('font', family='NanumGothic') # 폰트 설정
mpl.rc('axes', unicode_minus=False) # 유니코드에서 음수 부호 설정

# 차트 스타일 설정
sns.set(font="NanumGothic", rc={"axes.unicode_minus":False}, style='darkgrid')
plt.rc("figure", figsize=(10,8))
warnings.filterwarnings("ignore")

movies = pd.read_csv("movies_popular_genre.csv")

col_lst = [ 'movie_id','title', 'genre_ids', 'vote_average', 'vote_count', 'popularity', 'poster_path','overview',]
movies_df = movies[col_lst]
pd.reset_option("max_colwidth")

movies_df['genre_ids'].apply(literal_eval)[0]
movies_df['genres_literal'] = movies_df['genre_ids'].apply(lambda x : ('').join(x))

count_vect = CountVectorizer(min_df=0, ngram_range=(1,2))
genre_mat = count_vect.fit_transform(movies_df['genres_literal'])
genre_sim = cosine_similarity(genre_mat, genre_mat)


def search_sim_movie(df,sim_matrix, top_n=13):
    title_index = df.tail(n=1).index.values[0]
   
    df["similarity"] = sim_matrix[title_index, :].reshape(-1,1)
    temp = df.sort_values(by="similarity", ascending=False)
    # print(temp[:10])
    final_index = temp.index.values[ : top_n]

    return df.iloc[final_index]
# print(search_sim_movie(search_df,search_sim,'레드',top_n=12))
def find_sim_movie(df, sim_matrix, title_name, top_n=12):
 
    # 입력한 영화의 index
    title_movie = df[df['title'] == title_name]
    # print(title_movie)
    title_index = title_movie.index.values
  
   
    # # 입력한 영화의 유사도 데이터 프레임 추가
    df["similarity"] = sim_matrix[title_index, :].reshape(-1,1)
    
    # # 유사도 내림차순 정렬 후 상위 index 추출
    temp = df.sort_values(by="similarity", ascending=False)
    final_index = temp.index.values[ : top_n]

    return df.iloc[final_index]
# print(find_sim_movie(search_df,search_sim,'레드',12))
def premium_movie_finder(df, sim_matrix, title_name, top_n=10):
    
    # 입력한 영화의 index
    title_movie = df[df['title'] == title_name]
    title_index = title_movie.index.values
    
    # 입력한 영화의 유사도 데이터 프레임 추가
    df["similarity"] = sim_matrix[title_index, :].reshape(-1,1)
        
    # 유사도와 가중 평점순으로 높은 상위 index 추출 (자기 자신 제거)
    temp = df.sort_values(by=["similarity", "weighted_vote"], ascending=False)
    temp = temp[temp.index.values != title_index]
    
    final_index = temp.index.values[:top_n]
    
    return df.iloc[final_index]   






# ------------------------------------------------------
percentile = 0.6
m = movies_df['vote_count'].quantile(percentile)
C = movies_df['vote_average'].mean()

def weighted_vote_average(record):
    v = record['vote_count']
    R = record['vote_average']
    
    return ( (v/(v+m)) * R ) + ( (m/(m+v)) * C )   

movies_df['weighted_vote'] = movies_df.apply(weighted_vote_average, axis=1)

temp = movies_df[['title','vote_average','vote_count','weighted_vote']]
temp.sort_values('weighted_vote', ascending=False)[:10]





# -----------------------------------------------------------------

# 장르 유사도가 높은 영화 추천.
@api_view(['POST'])
@permission_classes([AllowAny])
def recmovie(request):
    request.data['movieId']
    movies = Movie.objects.filter(movie_id=request.data['movieId'])
    targetmovie = movies.values()[0]['title']
    # print(movies)
    # print(targetmovie)
    js = find_sim_movie(movies_df,genre_sim,targetmovie,4).to_json(orient = 'records', force_ascii=False)
    js_dic = literal_eval(js)
    for i in range(len(js_dic)):
        js_dic[i]['poster_path'] = js_dic[i]['poster_path'][1:] 
    
    return Response(js_dic[1:])


@api_view(['POST'])
def premiumrecmovie(request):
    # print(request.data)
    movie = Movie.objects.filter(movie_id=request.data['movieId'])
    
    targetmovie = movie.values()[0]['title']
    # print(premium_movie_finder(movies_df,genre_sim,targetmovie,10))
    js = premium_movie_finder(movies_df,genre_sim,targetmovie,10).to_json(orient = 'records', force_ascii=False)
    js_dic = literal_eval(js)
    
    return Response(js_dic)

@api_view(['GET'])
@permission_classes([AllowAny])
def search(request,what,searchvalue):

    if request.method== 'GET':
        if what == 'title':
            search = [searchvalue]*(len(col_lst)+2)
            search_df = movies_df.append(pd.Series(search, index=movies_df.columns), ignore_index=True)

            search_mat = count_vect.fit_transform(search_df['title'])
            search_sim = cosine_similarity(search_mat, search_mat)
            
            js = search_sim_movie(search_df,search_sim,13).to_json(orient = 'records', force_ascii=False)
            js_dic = literal_eval(js)
            print(js_dic)
            for i in range(len(js_dic)):
                js_dic[i]['poster_path'] = js_dic[i]['poster_path'][1:]
            
            return Response(js_dic[1:])
        



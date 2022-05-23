# 핫 바나나s



## 한 줄 소개

#### **`커뮤니티적 요소를 포함한 영화 추천 사이트`**



## 기획 배경

1. 수 많은 영화 중 어느 영화를 시청할 지 추천 or 소개를 해주는 서비스의 필요를 느낌
2. 영화 시청 뿐만 아니라 관련된 정보 혹은 이야기를 공유할 공간의 필요성
3. 타인의 주관적인 영화 평가에 대한 궁금증



## 기획 의도

1. 핫 바나나s 는 로튼 토마토와 같이 유저의 평점과 견해가 주를 이루는 사이트를 만들고자 개발을 기획하게 되었습니다.



## 서비스 특징

1. 검증된 유저를 판단하기 위해 포인트 제도를 도입하여, 사용자가 읽는 리뷰의 작성자에 대한 신뢰성을 향상시켰습니다.
2. 아이템 기반 필터링을 통해 사용자가 더 흥미를 느낄 수 있는 영화를 소개할 수 있도록 하였습니다.





## 팀 소개

#### 팀 정보

곽동현, 이혜진

#### 역할

- 곽동현 (BACK-END)
  - Django API Server, 영화 추천 Algorithm 개발
  - 데이터베이스 구축
- 이혜진 (FRONT-END)
  - Vue를 이용한 서버(Django, API)와 클라이언트간 통신, 데이터 관리
  - 핵심 UI 개발





## 프로젝트 진행기간

-  2021.11.17 ~ 2021.11.26 (10일)



## 주요 협업 툴

- MatterMost
- Notion



## 영화 추천 알고리즘 관련 코드



#### 기본 설정

```PYTHON
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



        
```



#### 유사도 조사

```python
# 검색 데이터 유사도 조사
def search_sim_movie(df,sim_matrix, top_n=13):
    title_index = df.tail(n=1).index.values[0]
   
    df["similarity"] = sim_matrix[title_index, :].reshape(-1,1)
    temp = df.sort_values(by="similarity", ascending=False)
    # print(temp[:10])
    final_index = temp.index.values[ : top_n]

    return df.iloc[final_index]


# 검색 데이터 분석
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
        
        
# 영화 장르 데이터 유사도 조사
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

```



#### 프리미엄 영화 추천 기능

```python
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

@api_view(['POST'])
def premiumrecmovie(request):
    # print(request.data)
    movie = Movie.objects.filter(movie_id=request.data['movieId'])
    
    targetmovie = movie.values()[0]['title']
    # print(premium_movie_finder(movies_df,genre_sim,targetmovie,10))
    js = premium_movie_finder(movies_df,genre_sim,targetmovie,10).to_json(orient = 'records', force_ascii=False)
    js_dic = literal_eval(js)
    
    return Response(js_dic)


```



#### 장르별 영화 추천

```python
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
```



#### 평점 갯수를 가중치로한 평점 칼럼 추가

```PYTHON
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
```


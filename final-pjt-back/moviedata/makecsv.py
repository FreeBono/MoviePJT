import requests, json, csv
from tmdb import TMDBHelper
import pandas as pd

#잠정 폐쇄
# with open('movies/fixtures/genre.json', 'rt', encoding='UTF8') as file:
#     realData = json.load(file)
# # print(realData)
# tmdb_helper = TMDBHelper('043ba4036363b1f15534a85a719d4706')
# # data = []

# for i in range(1, 2):
#     request_url = tmdb_helper.get_request_url('/movie/popular',language='ko-KR', page=str(i))
#     data = requests.get(request_url).json()
#     result = []
#     # print(data['results'])
#     for dic in data['results']:
#         if (not dic['overview']) or (not dic['poster_path']) or (not dic['vote_average']) or (not dic['popularity'] or (not dic['backdrop_path'])):
#             continue
#         else:
#             result.append(dic)

#     for p in range(len(result)):
#         for j in range(len(result[p]['genre_ids'])):
#             for k in range(len(realData)):
#                 if result[p]['genre_ids'][j] == realData[k]['id']:
#                     result[p]['genre_ids'][j] = realData[k]['name']




#     df = pd.json_normalize(result)
  
#     if i == 1:
#         info = df
         
#     else:
#         info = info.append(df, ignore_index=True)
   

#     # print(type(df))

# info.to_csv("test.csv", header=True,encoding='utf-8-sig')

# with open("data.csv", "w", encoding='UTF8') as f:
#     csv.dump(data, f, ensure_ascii=False, )
import requests
import json
from tmdb import TMDBHelper

with open('movies/fixtures/genre.json', 'rt', encoding='UTF8') as file:
    realData = json.load(file)
# print(realData)

# def get_genres():
#     """
#     장르 id, name
#     """
#     # TMDBHelpler 클래스의 인스턴스 tmdb_helper 생성
#     tmdb_helper = TMDBHelper('b763351a06f81e09443caceaed36e44e')

#     # 인스턴스 메서드 get_request_url를 이용해 필요한 url 생성
#     url = tmdb_helper.get_request_url('/genre/movie/list', language='ko-KR')

#     # requests를 이용하여 url에 요청을 보내고 json으로 변환
#     data = requests.get(url).json()

#     # 필요한 results만 반환 --> list
#     return (data['genres'])

# def get_popular_movie(page):
#     """
#     popular 영화목록 전체 조회
#     total_page: 500
#     total_results: 10000 (500 * 20)
#     """
#     # TMDBHelpler 클래스의 인스턴스 tmdb_helper 생성
#     tmdb_helper = TMDBHelper('b763351a06f81e09443caceaed36e44e')

#     # 인스턴스 메서드 get_request_url를 이용해 필요한 url 생성
#     url = tmdb_helper.get_request_url('/movie/popular', language='ko', region='KR', page=page)

#     # requests를 이용하여 url에 요청을 보내고 json으로 변환
#     data = requests.get(url).json()

#     # 필요한 results만 반환 --> list
#     return data['results']

# result = []
# for i in range(1, 501):
#     popular_movies = get_popular_movie(i)
#     for dic in popular_movies:
#         if (not dic['overview']) or (not dic['poster_path']) or (not dic['vote_average']) or (not dic['popularity'] or (not dic['backdrop_path'])):
#             continue
#         else:
#             movielist = []
#             info = {}
#             info["model"] = "movies.Movie"
#             info["fields"] = {}
#             for key, value in dic.items():
#                 if key == 'id':
#                     key = 'movie_id'
#                 info["fields"][key] = value
#             movielist.append(info)
#             result += movielist
# for i in range(len(result)):
#     for j in range(len(result[i]['fields']['genre_ids'])):
#         for k in range(len(realData)):
#             if result[i]['fields']['genre_ids'][j] == realData[k]['id']:
#                 result[i]['fields']['genre_ids'][j] = realData[k]['name']


# # popular순 영화 json 만들기
# with open('movies_popular_genre.json', 'w', encoding="utf-8") as make_file:
#     json.dump(result, make_file, ensure_ascii=False, indent="\t") 

# 장르 변환






def get_upcoming_movie(page):
    """
    popular 영화목록 전체 조회
    total_page: 500
    total_results: 10000 (500 * 20)
    """
    # TMDBHelpler 클래스의 인스턴스 tmdb_helper 생성
    tmdb_helper = TMDBHelper('b763351a06f81e09443caceaed36e44e')

    # 인스턴스 메서드 get_request_url를 이용해 필요한 url 생성
    url = tmdb_helper.get_request_url('/movie/upcoming', language='ko', region='KR', page=page)

    # requests를 이용하여 url에 요청을 보내고 json으로 변환
    data = requests.get(url).json()

    # 필요한 results만 반환 --> list
    return data['results']

result2 = []
# print(get_upcoming_movie(1))
for i in range(1, 5):
    popular_movies = get_upcoming_movie(i)
    for dic in popular_movies:
        if (not dic['overview']) or (not dic['poster_path']) or (not dic['vote_average']) or (not dic['popularity'] or (not dic['backdrop_path'])):
            continue
        else:
            movielist = []
            info = {}
            info["model"] = "movies.UpcomingMovie"
            info["fields"] = {}
            for key, value in dic.items():
                if key == 'id' :
                    key = 'movie_id'
                info["fields"][key] = value
            movielist.append(info)
            result2 += movielist
for i in range(len(result2)):
    for j in range(len(result2[i]['fields']['genre_ids'])):
        for k in range(len(realData)):
            if result2[i]['fields']['genre_ids'][j] == realData[k]['id']:
                result2[i]['fields']['genre_ids'][j] = realData[k]['name']

with open('movies_upcoming.json', 'w', encoding="utf-8") as make_file:
    json.dump(result2, make_file, ensure_ascii=False, indent="\t") 



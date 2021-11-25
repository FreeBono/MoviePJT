import json
import csv
# music.json 파일을 읽어서 melon.csv 파일에 저장
with open('movies_popular_genre.json', 'r', encoding = 'utf-8') as input_file, open('movies_popular_genre.csv', 'w', newline = '',encoding = 'utf-8') as output_file :
    data = json.load(input_file)
    '''
    data[0] 은 json 파일의 한 줄을 보관 {"title:"Super Duper", "songId": ...}
    data[0]['컬럼명'] 은 첫 번째 줄의 해당 컬럼 element 보관
    '''
    f = csv.writer(output_file)
    # csv 파일에 header 추가
    f.writerow(["adult", "backdrop_path", "genre_ids", "movie_id",
    "original_language","original_title","overview","popularity",
    "poster_path","release_date","title","video","vote_average","vote_count"
    ])
    # 노래 제목에 아래 문구가 포함 되어있을 경우 csv 저장하지 않음
    # write each row of a json file
   
    # exclude instrument versions
    for i in range(len(data)):
        f.writerow([data[i]['fields']["adult"], data[i]['fields']["backdrop_path"], data[i]['fields']["genre_ids"],data[i]['fields']["movie_id"],
        data[i]['fields']["original_language"], data[i]['fields']["original_title"], data[i]['fields']["overview"], data[i]['fields']["popularity"],
        data[i]['fields']["poster_path"], data[i]['fields']["release_date"], data[i]['fields']["title"], data[i]['fields']["video"],
        data[i]['fields']["vote_average"], data[i]['fields']["vote_count"]])

    
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# DB
client = MongoClient('mongodb+srv://anwjsrlrhwkd:<password>@cluster0.da3km.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta

# 크롤링
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')


# 구조적 가상 클래스 선택자는 리스트 반복문으로 일관처리
movies = soup.select('#old_content > table > tbody > tr')
for movie in movies:
    a = movie.select_one('td.title > div > a')
    if a is not None:
        point = movie.select_one('td.point')
        rank = movie.select_one('td:nth-child(1) > img')['alt']

        # 크롤링한 데이터 DB에 저장
        doc = {
            'rank': rank,
            'title': a.text,
            'star': point.text}
        # print(doc)
        # db.movies.insert_one(doc)

# DB에서 데이터 가져오기
print(db.movies.find_one({'title': '가버나움'})['star'])

target = db.movies.find_one({'title': '가버나움'})['star']
for data in db.movies.find({'star': target}):
    print(data['title'])

# DB데이터 변경
# db.movies.update_one({'title': '가버나움'}, {'$set': {'star':'0'}})

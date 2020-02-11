from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('memo.html')


@app.route('/bookmark', methods=['POST'])
def bookmark_post():
    try:
        # 1. 클라이언트가 보내준 url을 받기
        url = request.form['url']

        # 2. 그 url의 내용을 가져오기
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url, headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')

        og_image = soup.select_one('meta[property="og:image"]')
        og_title = soup.select_one('meta[property="og:title"]')
        og_description = soup.select_one('meta[property="og:description"]')

        # 3. 그 url의 내용에서 title, image, desc 을 찾아오기 (bs4)
        url_image = og_image['content']
        url_title = og_title['content']
        url_description = og_description['content']

        # 4. 그래서 그걸로 doc 을 만들
        doc = {
            'title': url_title,
            'image': url_image,
            'desc': url_description,
            'url': url,
        }
        db.bookmarks.insert_one(doc)
    except:
        return jsonify({'result': 'fail', 'msg': '이 요청은 POST!'})

    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/bookmark', methods=['GET'])
def bookmark_get():
    bookmarks = list(db.bookmarks.find({}, {'_id': False}))
    return jsonify(bookmarks)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

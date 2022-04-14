from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://anwjsrlrhwkd:wmfrlwk0@cluster0.da3km.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    bucket_list = list(db.bucket.find({}, {'_id': False}))
    count = len(bucket_list) + 1

    doc = {
        'num': count,
        'bucket': bucket_receive,
        'done': 0
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': '저장 완료'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    # 가져온 데이터가 문자열, 형변환 필요
    num_receive = int(request.form['num_give'])
    print(db.bucket.find_one({'num': num_receive}))
    db.bucket.update_one({'num': num_receive}, {'$set': {'done': 1}})
    return jsonify({'msg': '수정 완료'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    data = list(db.bucket.find({}, {'_id': False}))
    return jsonify({'orders': data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
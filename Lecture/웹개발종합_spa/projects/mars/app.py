from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://anwjsrlrhwkd:wmfrlwk0@cluster0.da3km.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    addr_receive = request.form['addr_give']
    size_receive = request.form['size_give']
    doc = {
        'name': name_receive,
        'addr': addr_receive,
        'size': size_receive
    }
    db.mars.insert_one(doc)
    return jsonify({'msg': 'POST 연결 완료!'})


@app.route("/mars", methods=["GET"])
def web_mars_get():
    db_mars = list(db.mars.find({}, {'_id': False}))
    return jsonify({'orders': db_mars})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
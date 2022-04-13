from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def mypage():
   return render_template('index.html')

@app.route('/test', methods=['POST'])
def test_post():
   # POST와 전달된 데이터 가져오기
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5001,debug=True)
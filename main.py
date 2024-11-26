from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return """
        <html><body>
        <form action="/hello" method="GET">
          名前: <input type="text" name="name"><br>
          ひとこと： <input type="text" name="comment"><br>
          <input type="submit" value="送信">
        </form>
        </body></html>
    """

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None: name = '名無し'

    comment = request.args.get('comment', '') 

    cuisines = ['フランス料理', 'イタリア料理', '中華料理', '日本料理']
    recommended_cuisine = random.choice(cuisines)

    return """
    <h1>{0}さん、こんにちは！</h1>
    <p>ひとこと: {1}</p>
    <p>本日のおすすめランチは「{2}」です！</p>
    """.format(name, comment, recommended_cuisine)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
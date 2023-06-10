from flask import Flask
from datetime import datetime

print(__name__)

app = Flask(__name__)


@app.route("/book/<int:id>")
def book(id):
    try:
        books = {1: "Python", 2: "Java", 3: "C++"}
        return books[id]
    except Exception as e:
        print(e)
        return "沒有書籍資料"


@app.route("/today")
def today():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f'<h1>{datetime.now()}</h1>'


@app.route("/index")
@app.route("/")
def index():
    return 'Hello Flask123!'


app.run(debug=True)

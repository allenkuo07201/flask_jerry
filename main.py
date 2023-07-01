from flask import Flask, render_template
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


# app.run(debug=True)

# 2023/7/1   start

def get_today():
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    return date


@app.route("/stock")
def stock():
    stocks = [
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
    ]
    for stock in stocks:
        print(stock["分類"], stock["指數"])

    return render_template("stock.html", date=get_today(), stocks=stocks)


if __name__ == "__main__":
    # print(get_bmi(167, 67.5))

    app.run(debug=True)

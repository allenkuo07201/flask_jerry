import requests
from bs4 import BeautifulSoup


def get_stock():

    url = 'https://tw.stock.yahoo.com/'

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    lis = soup.find('nav', class_="indexChartNav").find_all('li')

    stocks = []
    for li in lis:
        # 取前2個資訊
        spans = li.find_all('span')[:2]
        # 組合成字典
        data = {"分類": spans[0].text.strip(), "指數": spans[1].text.strip()}
        # 加入外部串列
        stocks.append(data)
    # print(stocks)
    return stocks


if __name__ == "__main__":
    print(get_stock())

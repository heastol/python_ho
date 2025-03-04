import requests as req
from bs4 import BeautifulSoup as bs
url = "https://www.melon.com/chart/index.htm"
headers = {}
web = req.get(url, headers = headers)
def mel():
    soup = bs(web.content, 'html.parser')
    title = soup.select('.rank01')
    name = soup.select('.checkEllipsis a')
    str = ''
    for i, (t, n) in enumerate(zip(title, name), 1):
        str += f'{i}위 : {t.text.strip()} / {n.text}\n'
    print(str, end=' ')

if __name__ == '__main__':
    mel()
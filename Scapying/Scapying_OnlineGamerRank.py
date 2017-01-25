# 巴哈姆特的OnlineGame排行
import requests
from bs4 import BeautifulSoup

gameRank = requests.get(
    'https://acg.gamer.com.tw/billboard.php?t=2&p=OLG', params=None)
gameRank.encoding = 'UTF-8'
soup = BeautifulSoup(gameRank.text, "html.parser")
for game in soup.findAll(class_='ACG-mainbox1'):
    print(game.find(class_='ACG-mainumber').string + ' ' +
          game.find(class_='ACG-maintitle').find('a').string)
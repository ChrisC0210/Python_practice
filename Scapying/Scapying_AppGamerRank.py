# 用來爬巴哈姆特的AndroidAPP排行
import requests
from bs4 import BeautifulSoup
game_raking_html = requests.get(
    'https://acg.gamer.com.tw/billboard.php?t=2&p=Android')
game_raking_html.encoding = 'UTF-8'
soup = BeautifulSoup(game_raking_html.text, "html.parser")
# 抓取class_='ACG-mainbox1'內部class_='ACG-maintitle'中的<a>
# 不過註解掉好像也沒差
# soup.find(class_='ACG-mainbox1').find(class_='ACG-maintitle').find('a').string
# 印出
for game in soup.findAll(class_='ACG-mainbox1'):
    print(game.find(class_='ACG-mainumber').string + ' ' +
          game.find(class_='ACG-maintitle').find('a').string)

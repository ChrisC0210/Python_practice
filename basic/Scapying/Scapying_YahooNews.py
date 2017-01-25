#YAHOO新聞爬蟲

#爬蟲Model
import requests
#處裡資料的Model
from bs4 import BeautifulSoup
#爬蟲的目標網址
yahoo_news_xml = requests.get('https://tw.news.yahoo.com/rss/technology')
#指定編碼是UTF-8
yahoo_news_xml.encoding = 'UTF-8'
#用parser解析HTML
soup = BeautifulSoup(yahoo_news_xml.text, "html.parser")
soup.title

#這是(BeautifulSoup成功)?<class 'bs4.BeautifulSoup'>:else
#type(soup)

#跑迴圈把所有<item>的資料扔進news裡
for news in soup.findAll('item'):
	#把news裡的title都印出，並使用.string方法把HTML code篩掉
	print(news.title.string)
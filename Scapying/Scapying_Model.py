#做好了令存新檔！
import requests
from bs4 import BeautifulSoup
blog_url = requests.get('https://ray247k.wordpress.com/')
blog_url.encoding = 'UTF-8'
soup = BeautifulSoup(blog_url.text, "html.parser")

for blog_title in soup.findAll(class_='entry-title'):
	print(blog_title.string)


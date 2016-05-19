from bs4 import BeautifulSoup
from urllib import request


url = 'https://www.brainyquote.com/quotes/authors/w/william_shakespeare.html'
#site_url = "http://kittify.herokuapp.com/#"
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent,}

quote_request = request.Request(url, headers=headers)
response = request.urlopen(quote_request)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
print(soup)

quote_containers = soup.find_all(class_='bqQuoteLink')
for quote_container in quote_containers:
	quote = quote_container.a.contents[0]
	print(quote)

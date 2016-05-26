from app import db, ShakespeareQuote
from bs4 import BeautifulSoup
from urllib import request

def craw_brainy_quotes():
	domain = 'https://www.brainyquote.com'
	relative_path = '/quotes/authors/w/william_shakespeare.html'
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers = {'User-Agent': user_agent,}
	url = domain + relative_path

	while url is not None:
		quote_request = request.Request(url, headers=headers)
		response = request.urlopen(quote_request)

		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')

		quote_containers = soup.find_all(class_='bqQuoteLink')
		for quote_container in quote_containers:
			quote = quote_container.a.contents[0]
			add_quote_database(quote, url)

		try:
			paginations = soup.find_all(class_='pagination')
			if len(paginations) > 0:
				first_pagination = paginations[0]
				links_to_quotes = first_pagination.find_all('li')
				last_li = first_pagination.find_all('li')
				next_button = links_to_quotes[len(links_to_quotes)-1]
				next_button_link = next_button.a
				assert(next_button_link.contents[0] == 'Next')

				relative_path_to_next_page = next_button_link.get('href')
				url = domain + relative_path_to_next_page
			else:
				url = None
		except:
			url = None


def add_quote_database(quote, source_url):
	quote = ShakespeareQuote(quote=quote, source_url=source_url)
	quote.save()


if __name__ == "__main__":
	craw_brainy_quotes()

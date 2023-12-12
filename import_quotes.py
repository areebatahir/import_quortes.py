import requests
from bs4 import BeautifulSoup
def scrape_quotes(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        for quote, author in zip(quotes, authors):
            print(f"Quote: {quote.text}")
            print(f"Author: {author.text}")
            print(f"----------------------")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Time Out: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
if __name__ == '__main__':
    scrape_url = 'http://quotes.toscrape.com/page/2/'
    scrape_quotes(scrape_url)

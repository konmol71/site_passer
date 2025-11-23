import requests
import bs4

class BasePasser:
    site_url: str = 'https://upl.uz'

    def get_soup(self, url: str=site_url) -> bs4.BeautifulSoup:
        html = requests.get(url).text
        return bs4.BeautifulSoup(html, 'html.parser')
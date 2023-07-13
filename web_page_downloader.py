import requests
from bs4 import BeautifulSoup

class PageDownloader:
    def get_html_from_website(self, url : str) -> str:
        return requests.get(url).text

    def save_html(self, filename : str, html_content : str) -> None:
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(html_content)
    
    def remove_scripts_from_html(self, html_content : str) -> str:
        soup = BeautifulSoup(html_content, 'html.parser')

        for script in soup.find_all('script'):
            script.extract()

        for script in soup.find_all('script', {'src': True}):
            script.extract()

        return str(soup)

    def save_html_from_url(self, url : str, html_filename : str) -> None:
        html = self.get_html_from_website(url)
        html = self.remove_scripts_from_html(html)
        self.save_html(html_filename, html)

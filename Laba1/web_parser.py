from bs4 import BeautifulSoup
import requests

class WebParser:
    def __init__(self, url):
        self.url = url
        self.cafedry = []

    def parse(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, "html.parser")
        print(page.status_code)  # смотрим ответ

        for caf in soup.select('div#pagecontent > ul > li > a'):
            self.cafedry.append(caf.text)

    def get_cafedry(self):
        return self.cafedry

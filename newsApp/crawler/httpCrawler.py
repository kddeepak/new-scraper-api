import requests
from newsApp.models import Articles


class HttpCrawler:
    @staticmethod
    def crawl(url, headers):
        response = requests.get(url, headers=headers)
        return response.content

    def saveToTables(self):
        article = Articles()


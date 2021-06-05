import requests
from newsApp.models import Articles


class HttpCrawler:
    @staticmethod
    def crawl(url, headers):
        response = requests.get(url, headers=headers)
        return response.content

    def saveToTables(self,site_url, story_date , category , description, title, image_url, created_at):
        article = Articles(site_url =site_url, story_date = story_date, category = category,
                              description = description, title = title, image_url = image_url, created_at = created_at)
        article.save()



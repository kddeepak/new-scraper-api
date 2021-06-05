from newsApp.crawler.httpCrawler import HttpCrawler
from .parsedNewsContent import ParsedNewsContent
from bs4 import BeautifulSoup
import time
from newsApp.models import Articles


class TimesOfIndiaScraper(HttpCrawler):

    def __init__(self):
        self.image_url_selector = ""
        self.story_date_selector = ""
        self.category_selector = ""
        self.source_selector = ""
        self.author_name_selector = ""
        self.description_selector = ""
        self.title_selector = ""

    def getCrawlContent(self, url):
        headers = {}
        response = HttpCrawler.crawl(url, headers)
        soup = BeautifulSoup(response, 'html5lib')
        self.dom = soup
        self.getAllNewsDiv()
        return response

    def getTitle(self, element):
        title = element.select(self.title_selector)
        if len(title) > 0:
            title = title[0].get_text()
            return title
        return None

    def getDescription(self, element):
        description = element.select(self.description_selector)
        if len(description) > 0:
            description = description[0].get_text()
            return description
        return None

    def getImageUrl(self, element):
        image_url = element.select(self.image_url_selector)
        if len(image_url) > 0:
            image_url = image_url[0].get_text()
            return image_url
        return None

    def getAuthorName(self, element):
        author = element.select(self.author_name_selector)
        if len(author) > 0:
            author = author[1].get_text()
            return author
        return None

    def getCategory(self, element):
        category = element.select(self.category_selector)
        if len(category) > 0:
            category = category[0].get_text()
            return category
        return None

    def getAllNewsDiv(self):
        dom = self.dom
        print(self.news_element_div_selector)
        elements = dom.select(self.news_element_div_selector)
        parsed_news_list = []
        for element in elements:
            # print(element)
            title = self.getTitle(element)
            description = self.getDescription(element)
            print(description)
            author = self.getAuthorName(element)
            print(author)
            category = self.getCategory(element)
            print(category)
            image_url = self.getImageUrl(element)
            print(image_url)
            parsed_content = ParsedNewsContent(title=title, desc=description, author=author,
                                               category=category, image_url=image_url,
                                               website_name=self.website_name, timestamp=time.time())
            parsed_news_list.append(parsed_content)

from flask import jsonify, request
from bs4 import BeautifulSoup
from newsApp import app
from .models import Articles
from .scraper.yahooFinanceScraper import YahooFinanceScraper

@app.route("/ping")
def hello_world():
    return "Pong"

@app.route("/getAllArticles")
def get_all():
    articles = Articles.objects()
    return jsonify(articles.to_json())

@app.route("/scrape/gethtml")
def crawl_and_scrape():
    url = request.args.get('url')
    yahoo_scraper = YahooFinanceScraper()
    res = yahoo_scraper.getCrawlContent(url = url)
    soup = BeautifulSoup(res,'html5lib')
    return soup.prettify()

@app.route("/getByAuthor/<author>")
def get_author_article():
    pass

@app.route("/getByDate")
def get_articles_by_date():
    pass
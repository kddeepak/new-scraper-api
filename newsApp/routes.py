from flask import jsonify
from bs4 import BeautifulSoup
from newsApp import app
from .models import Articles
from .scraper.yahooFinanceScraper import YahooFinanceScraper

@app.route("/ping")
def hello_world():
    article = Articles(site_url ="yahoo.finance.in")
    article.save()
    return jsonify(article.to_json())

@app.route("/getAll")
def get_all():
    articles = Articles.objects()
    return jsonify(articles.to_json())

@app.route("/scrape")
def crawl_and_scrape():
    yahoo_scraper = YahooFinanceScraper()
    res = yahoo_scraper.getCrawlContent(url = "https://in.finance.yahoo.com")
    soup = BeautifulSoup(res,'html5lib')
    return soup.prettify()

from newsApp.scraper import scraperFactory
import logging


def worker():
    with open("news_sites.txt") as f:
        content = f.readlines()
    sites = [x.strip() for x in content]

    for site in sites:
        try:
            print(site)
            scraper_obj = scraperFactory.ScraperFactory.getScraper(site)
            scraper_obj.getCrawlContent(site)
        except:
            logging.error('Scraper Worker Failed!!')

from . import yahooFinanceScraper, timesOfIndiaScraper


class ScraperFactory:

    @staticmethod
    def getScraper(self, site):
        site_map = {
            "https://in.finance.yahoo.com": yahooFinanceScraper.YahooFinanceScraper(),
            "https://timesofindia.indiatimes.com/": timesOfIndiaScraper.TimesOfIndiaScraper()
        }
        if site in site_map.keys():
            return site_map[site]
        else:
            return None

from classes import WebScraperController

class MainController:
    def __init__(self):
        self.web_scraper = WebScraperController()
    
    def get_prices(self, json):
        return {
            "amazon": 11.1,
            "lazada": 20.1,
            "shopee": 10.3
        }
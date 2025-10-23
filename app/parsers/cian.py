import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from app.core.source import CIAN_BASE_URL, CIAN_HEADERS, CIAN_COOKIES
from .base_parser import BaseParser


class CianParser(BaseParser):
    def __init__(self):
        self.session = requests.Session()
        self.ua = UserAgent()
        self.base_url = CIAN_BASE_URL
        self.request_count = 0

        self.set_session()
    
    def __del__(self):
        self.session.close()

    def get_headers(self):
        headers = CIAN_HEADERS.copy()
        headers["user_agent"] = self.ua.random
        return headers

    def get_cookies(self):
        return CIAN_COOKIES
    
    def set_session(self):
        self.session.headers.update(self.get_headers())
        self.session.cookies.update(self.get_cookies())

    def get_request(self, url):
        self.request_count += 1
        try:
            request = self.session.get(url)
            print(f"Запрос {self.request_count} к {url} - Статус: {request.status_code}")
            return request
        except requests.exceptions.RequestException as e:
            print(f"Ошибка: {e}")
            
        return None

    def parse_appartments_list(self, url=None):
        url = url or f"{self.base_url}/snyat-kvartiru/"

        request = self.get_request(url)
        src = request.text

        soup = BeautifulSoup(src, "lxml")
        all_ad = soup.find_all(attrs={"data-testid": "offer-card"})

        ad_data_list = []

        for ad in all_ad:
            ad_url = ad.find("a", class_="_93444fe79c--media--9P6wN").get("href")
            
            id = ad_url.split("/")[-2]

            try:
                ad_title = ad.find("span", attrs={"data-mark": "OfferTitle"}).find("span").text
            except:
                ad_title = "No title"

            try:
                ad_rent = ad.find("span", attrs={"data-mark": "MainPrice"}).find("span").text
            except:
                ad_rent = "No rent"

            try:
                ad_rent_description = ad.find("p", attrs={"data-mark": "PriceInfo"}).text
            except:
                ad_rent_description = "No rent description"
            
            try:
                ad_adress_tegs = ad.find_all("a", attrs={"data-name": "GeoLabel"})
                ad_adress = ""
                for tegs in ad_adress_tegs:
                    ad_adress += tegs.text + " "
            except:
                ad_adress = "No adress"
            
            try:
                ad_description = ad.find("div", attrs={"data-name": "Description"}).find("p").text
            except:
                ad_description = "No description"
            
            try:
                ad_time = ad.find("div", attrs={"data-name": "TimeLabel"}).find("div", class_="_93444fe79c--absolute--yut0v").find("span").text
                ad_time = ad_time.lower()
                now = datetime.now().strftime("%d.%m.%Y")
                if "сегодня" in ad_time:
                    ad_time = ad_time.replace("сегодня", str(now))
                elif "вчера" in ad_time:
                    delta = timedelta(days=1) 
                    ad_time = ad_time.replace("вчера", str(now - delta))
            except:
                ad_time = "No time"

            ad_data_list.append(
                {
                    "external_id": id,
                    "source": 'Cian',
                    "title": ad_title,
                    "url": ad_url,
                    "adress": ad_adress,
                    "rent": ad_rent,
                    "rent_description": ad_rent_description,
                    "description": ad_description,
                    "data": ad_time
                }
            )
        
        return ad_data_list

    
    

import requests
from parsel import Selector


class HouseCrawler:
    MAIN_URL = "https://www.house.kg/snyat"
    BASE_URL = "https://www.house.kg"

    def get_page(self):
        page = requests.get(url=HouseCrawler.MAIN_URL, timeout=10)
        self.page = page.text

    def get_house_link(self):
        html = Selector(text=self.page)
        links = html.css('p.title a::attr(href)').getall()
        links = list(map(lambda l: HouseCrawler.BASE_URL + l, links))
        return links[:5]

    def get_house_photo(self):
        html = Selector(text=self.page)
        photos = html.css('meta[itemprop="photo"]::attr(content)').getall()
        return photos[:5]

    def get_house_details(self):
        html = Selector(text=self.page)
        details = html.css('p.title a::text').getall()
        details = [detail.strip() for detail in details if detail.strip()]
        return details[:5]

    def get_house_address(self):
        html = Selector(text=self.page)
        address = html.css('div.address::text').getall()
        address = [addr.strip() for addr in address if addr.strip()]
        return address[:5]

# if __name__ == "__main__":
#     crawler = HouseCrawler()
#     crawler.get_page()
#     crawler.get_house_link()
#     crawler.get_house_photo()
#     crawler.get_house_details()
#     crawler.get_house_address()


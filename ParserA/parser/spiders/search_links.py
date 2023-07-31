import pandas as pd
import scrapy


def read_product_codes_from_excel(self, file_path):
    pass


class SearchLinksSpider(scrapy.Spider):
    name = "search_links"
    allowed_domains = ["absolut-tds.com"]
    start_urls = ["https://absolut-tds.com/search"]

    file_path = r"c:\Users\user\Desktop\Сопоставление.xlsx"

    def read_product_codes_from_excel(self):
        df = pd.read_excel(self)
        product_codes = df["Артикул Поставщика"].tolist()
        return product_codes

    product_codes = read_product_codes_from_excel(file_path)

    def start_requests(self):
        for code in self.product_codes:
            url = f"https://absolut-tds.com/search/?q={code}"
            yield scrapy.Request(url, callback=self.parse, meta={"product_code": code})

    def parse(self, response, **kwargs):
        product_code = response.meta.get("product_code")
        product_link = response.css("div.product-image a::attr(href)").get()

        if product_link:
            product_code = product_code
            product_link = "https://absolut-tds.com" + product_link

            yield {
                "product_code": product_code,
                "product_link": product_link,
            }
        else:
            # Если товар не найден, выведите сообщение
            self.logger.info(f"Товар с кодом {product_code} не найден.")
            yield {
                "product_code": product_code,
                "product_link": "Товар не найден",
            }

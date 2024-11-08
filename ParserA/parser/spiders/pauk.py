import json

import pandas as pd
import scrapy


def parse_post(response):
    # Обработка ответа POST-запроса
    item_id = response.meta.get("item_id")
    product_name = response.meta.get("product_name")
    price_name = response.meta.get("price_name")
    product_code = response.meta.get("product_code")
    count_data = json.loads(response.body)
    as_product_code = response.meta.get("as_product_code")
    url = response.meta.get("url")

    yield {
        "ID": item_id,
        "Название товара": product_name,
        "Цена товара": price_name,
        "Количество товара": count_data,
        "Код товара": product_code,
        "Артикул": as_product_code,
        "URL": url,
    }


# noinspection PyInterpreter
class PaukSpider(scrapy.Spider):
    name = "pauk"
    allowed_domains = ["absolut-tds.com"]
    start_urls = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        file_path = r"C:\Users\user\PycharmProjects\ParserAbsolut\ParserA\parser\Excel_files\Сопоставление.xlsx"
        self.df = pd.read_excel(file_path)
        urls = self.df["URL"].tolist()
        self.start_urls.extend(urls)
        # Загрузка таблицы с соответствиями "Артикул Поставщика" и кодами товаров
        self.df = pd.read_excel(file_path)
        # Преобразование в словарь для удобства поиска
        self.file_path_dict = dict(
            zip(self.df["Артикул Поставщика"], self.df["Артикул"])
        )

    def start_requests(self):
        for url in self.start_urls:
            item_id = url.split("/")[-2]
            yield scrapy.Request(
                url=url, callback=self.parse, meta={"item_id": item_id}
            )

    def parse(self, response, **kwargs):
        # Здесь ваш код для обработки текущей страницы
        item_id = response.meta.get("item_id")
        if response.css("div.product-item-details h1.product-item-name::text"):
            product_name = response.css(
                "div.product-item-details h1.product-item-name::text"
            ).get()
        else:
            product_name = "Нет данных о названии"

        if response.css(
            "div.product-item-details div.price-box:nth-child(4)::text"
        ).getall():
            price_name = response.css(
                "div.product-item-details div.price-box:nth-child(4)::text"
            ).getall()
        else:
            price_name = "Нет данных о цене"

        if response.css("div span.info-deta::text")[1].get():
            product_code = response.css("div span.info-deta::text")[1].get()
        else:
            product_code = "Нет кода товара"

        # Получение кодов товаров из соответствующей таблицы по "Артикулу Поставщика"
        as_product_code = self.file_path_dict.get(product_code, "Код товара не найден")

        # Выполнение POST-запроса
        url_post = "https://absolut-tds.com/ajax/shop/check_item_quantity.php"
        data = {
            "id": item_id,
        }

        yield scrapy.FormRequest(
            url_post,
            formdata=data,
            method="POST",
            callback=parse_post,
            meta={
                "item_id": item_id,
                "product_name": product_name,
                "price_name": price_name[1],
                "product_code": product_code,
                "as_product_code": as_product_code,
                "url": response.url,
            },
        )

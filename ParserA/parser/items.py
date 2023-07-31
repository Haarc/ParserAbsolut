# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ParserItem(scrapy.Item):
    # define the fields for your item here like:
    # product_id = scrapy.Field()
    # product_code = scrapy.Field()
    # product_name = scrapy.Field()
    # price_name = scrapy.Field()
    # count_data = scrapy.Field()

    pass

    # Добавим отладочный вывод, чтобы увидеть, что содержится в count_data
    # print(count_data)

    # df = pd.DataFrame(
    #     {
    #         "ID": [product_id],
    #         "Название товара": [product_name],
    #         "Код товара": [product_code],
    #         "Цена товара": [price_name],
    #         "Количество товара": [count_data],
    #     }
    # )

    # self.pandas_utilit(df)

    # def pandas_utilit(self, df):
    #     df2 = pd.read_excel(r'C:\Users\user\venv\Parser\Загруженные данные\Сопоставление_новое.xlsx')
    #     table_join = pd.merge(
    #         df,
    #         df2["Артикул"],
    #         on="Код товара",
    #         how="left"
    #     )

    #     table_join.to_excel(r"c:\Users\user\Desktop\Готовые данные.xlsx", index=False)

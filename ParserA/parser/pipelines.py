# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

class ParserPipeline:
    def process_item(self, item, spider):

        # product_id = item.get('product_id')
        # product_code = item.get('product_code')
        # product_name = item.get('product_name')
        # price_name = item.get('price_name')
        # count_data = item.get(count_data)


        # item['ID'] = product_id
        # item['Название'] = product_name
        # item['Код продукта'] = product_code
        # item['Цена'] = price_name
        # item['Кол-во'] = count_data

        return item
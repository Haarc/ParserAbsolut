from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from parser.spiders.pauk import PaukSpider
import shutil
import os
from datetime import datetime


def run():
    process = CrawlerProcess(get_project_settings())
    process.settings.set(
        "FEEDS",
        {"file:///C:/Work_parser_files/parsing.xlsx": {"format": "xlsx"}},
    )
    process.crawl(PaukSpider)
    process.start()


def save_and_remove():
    src = "C:/Work_parser_files/parsing.xlsx"
    dst1 = "C:/Users/user/Desktop/parsing"
    dst2 = "//SHS/Users/Public/Documents/OZON/Парсинг/"

    now = datetime.now().strftime("%d-%m-%Y")
    filename = f"parsing_{now}.xlsx"

    shutil.copy(src, f"{dst1}/{filename}")

    shutil.copy(src, f"{dst2}/парсинг.xlsx")

    os.remove(src)


if __name__ == "__main__":
    run()
    save_and_remove()

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from parser.spiders.pauk import PaukSpider
import os
def run_spider():
    process = CrawlerProcess()

    # Установите путь к папке, где хотите сохранить файл
    output_dir = r"C:\Users\user\Desktop\Инструкция"

    # Путь к файлу для сохранения
    file_name = "file.csv"
    file_path = os.path.join(output_dir, file_name)

    # Установите настройку FEED_URI для сохранения в указанный файл
    settings = get_project_settings()
    settings.set("FEED_URI", file_path)

    process.crawl(PaukSpider)
    process.start()

if __name__ == "__main__":
    run_spider()
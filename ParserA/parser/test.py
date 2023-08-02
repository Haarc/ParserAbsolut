import shutil

# Путь к файлу, который нужно скопировать
source_file_path = r"C:\Users\user\PycharmProjects\ParserAbsolut\ParserA\parser\Excel_files\Сопоставление1.xlsx"

# Путь, куда нужно скопировать файл
destination_file_path = r"\\shs\users\Public\Documents\OZON\Парсинг"

# Копирование файла
shutil.copy(source_file_path, destination_file_path)

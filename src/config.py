from configparser import ConfigParser
from typing import Dict


def config(filename="database.ini", section="postgresql") -> Dict :
    # создание парсера
    parser = ConfigParser()
    # чтение конфигурационного файла
    parser.read(filename, encoding="utf-8")
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
             f'Секция [{section}] не найдена в файле {filename}')
    return db
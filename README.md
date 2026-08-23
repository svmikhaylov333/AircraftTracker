# AircraftTracker
![Python Version](https://img.shields.io/badge/python-3.12+-blue)
![Status](https://img.shields.io/badge/status-development-blue)
![Style](https://img.shields.io/badge/code%20style-black-blue)
![Version](https://img.shields.io/badge/version-0.0.1-blue)

AircraftTracker - Трекер самолетов. 
Программа, которая собирает данные о самолетах в воздушных пространствах тех стран, которые вы выберете.
Чтобы получить географические координаты стран

## Содержание
- [Технологии](#технологии)
- [Установка](#установка)
- [Тестирование](#тестирование)
- [Deploy и CI/CD](#deploy-и-ci/cd)
- [Contributing](#contributing)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

## Технологии
- [GatsbyJS](https://www.gatsbyjs.com/)
- [TypeScript](https://www.typescriptlang.org/)
- ...

## Установка

```bash
# Клонировать репозиторий
git clone <repository-url>
cd /папка_с_прооектом/AircraftTracker
# Установить зависимости через poetry
poetry install
# Активировать виртуальное окружение
eval $(poetry env activate)
```

## Использование
Расскажите как установить и использовать ваш проект, покажите пример кода:

### Запуск программы
```bash
python main.py
```


## Разработка

### Требования
- Python 3.12+
- Poetry

### Установка зависимостей
Для установки зависимостей, выполните команду:
```bash
poetry install --no-root
```

### Запуск Development сервера
Чтобы запустить сервер для разработки, выполните команду:
```sh
npm start
```

### Создание билда
Чтобы выполнить production сборку, выполните команду: 
```sh
npm run build
```

## Тестирование
Для запуска проверки функций:

```bash
pytest
```
Дополнительные проверки
```bash
python tests/test.py
```
Для анализа покрытия кода тестами использовать

```bash
pytest --cov
```

Сформировать отчет, см. htmlcov/index.html
 ```bash
pytest --cov=src --cov-report=html
```
Сформировать отчет "без .gitignore", см. htmlcov/index.html
 ```bash
pytest --cov=src --cov-report=html; Remove-Item htmlcov/.gitignore
```
Если папка (не пустая) 'htmlcov' существует и в ней удален .gitignore. 
При повторных генерациях .gitignore не создается
---

## Deploy и CI/CD
На текущем этапе CI/CD отсутствует.

## Contributing
По вопросам и предложениям писать на почту.

## FAQ 
Ответы на вопросы...

### Зачем вы разработали этот проект?
Чтобы был.

## To do
- [x] Подготовка: Добавить крутое README. Наметить структуру
- [ ] Шаг 1: создание абстрактного класса для работы с API
- [ ] Шаг 2: создание класса для работы с информацией о самолетах
- [ ] Шаг 3: Создание классов для работы с файлами
- [ ] Шаг 4: создание функции для взаимодействия с пользователем
- [ ] Шаг 5: объединение компонентов

Объединить все классы и функции в единую программу.
Покрыть описанный функционал тестами.
- [ ] ...

## Команда проекта
MC

## Источники
...
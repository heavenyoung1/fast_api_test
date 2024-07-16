## Проект FastAPI

## Installing dependencies

You will need a recent version of Python to run this app.
To install project dependencies:

```
pip install -r requirements.txt
```
It is recommended to install dependencies into a [virtual env]

## Running the app

To run the app:

```
uvicorn app.main:app --reload
```

Then, open your browser to [`http://127.0.0.1:8000`](http://127.0.0.1:8000) to load the app.

## Reading the docs

To read the API docs, open the following pages:

* [`/docs`](http://127.0.0.1:8000/docs) for classic OpenAPI docs
* [`/redoc`](http://127.0.0.1:8000/redoc) for more modern ReDoc docs

* ## TODO list

* Automate API tests
* Automate UI tests
* Automate unit tests


## Дерево проекта

### Корневая директория
- `alembic/`
  - `versions/`
  - `env.py`
  - `README`
  - `script.py.mako`
- `app/`
  - `__pycache__/`
    - `__init__.cpython-312.pyc`
    - `crud.cpython-312.pyc`
    - `database.cpython-312.pyc`
    - `models.cpython-312.pyc`
    - `schemas.cpython-312.pyc`
  - `__init__.py`
  - `crud.py`
  - `database.py`
  - `models.py`
  - `schemas.py`
- `static/`
  - `__pycache__/`
  - `fonts/`
  - `icons/`
  - `image/`
  - `scripts.js`
  - `style.css`
  - `text.py`
- `templates/`
  - `about.html`
  - `index.html`
  - `navbar.html`
  - `project-item.html`
  - `skills.html`
- `venv/`
- `.gitignore`
- `alembic.ini`
- `main.py`
- `README.md`
- `requirements.txt`
- `sql_app.db`

## Описание директорий и файлов

- `alembic/`: Каталог для управления миграциями базы данных.
  - `versions/`: Поддиректория для хранения версий миграций.
  - `env.py`: Настройки окружения Alembic.
  - `README`: Документация Alembic.
  - `script.py.mako`: Шаблон скриптов миграции.

- `app/`: Основное приложение.
  - `__init__.py`: Инициализация пакета.
  - `crud.py`: Функции для выполнения CRUD операций.
  - `database.py`: Настройки подключения к базе данных.
  - `models.py`: Определение моделей базы данных.
  - `schemas.py`: Схемы данных для валидации и сериализации.

- `static/`: Статические файлы (CSS, JS, изображения и т.д.).
  - `fonts/`: Шрифты.
  - `icons/`: Иконки.
  - `image/`: Изображения.
  - `scripts.js`: Основной скрипт JavaScript.
  - `style.css`: Основной файл стилей CSS.
  - `text.py`: Файл с элементами данных python

- `templates/`: HTML шаблоны.
  - `about.html`: Страница "Обо мне".
  - `index.html`: Главная страница.
  - `navbar.html`: Шаблон навигационной панели.
  - `project-item.html`: Шаблон элемента проекта.
  - `skills.html`: Страница с навыками.

- `tests/`: Тесты.
  - `test_main.py` 
  - `test_crud.py`

- `venv/`: Виртуальное окружение Python.

- `.gitignore`: Файл для исключения файлов и директорий из системы контроля версий Git.

- `alembic.ini`: Конфигурационный файл Alembic.

- `main.py`: Основной файл запуска приложения.

- `README.md`: Документация проекта.

- `requirements.txt`: Список зависимостей Python.

- `sql_app.db`: База данных SQLite.

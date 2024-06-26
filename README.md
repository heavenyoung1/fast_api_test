##Тестовое название

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

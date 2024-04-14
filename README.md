python -m venv venv

pip install -r requirements.txt

Заполнение данных в .env для PostgreSQL как в файле .env.example

alembic revision --autogenerate # Миграции (опционально)

alembic upgrade head # Применение миграций

Находясь в главном каталоге проекта:

uvicorn "src.entrypoint:app" --reload или запустить файл entrypoint.py

Путь сваггера:
http://127.0.0.1:8000/docs

Путь редока:
http://127.0.0.1:8000/redoc
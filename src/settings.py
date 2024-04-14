import os
from pathlib import Path

from dotenv import load_dotenv

# Project dir

BASE_DIR = Path(__file__).parent.parent

load_dotenv(os.path.join(BASE_DIR, ".env"))

POSTGRES_USER = os.environ.get("POSTGRES_USER", default='postgres')
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", default='postgres')
POSTGRES_DB = os.environ.get("POSTGRES_DB", default='postgres')
DB_HOST = os.environ.get("DB_HOST", default='localhost')
DB_PORT = os.environ.get("DB_PORT", default=5432)

EMAIL_LOGIN = os.environ.get("EMAIL_LOGIN")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = os.environ.get("SMTP_PORT")

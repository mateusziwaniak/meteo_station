import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = {
    'host': os.getenv('METEO_DB_HOST'),
    'port': int(os.getenv('', 3306)),
    'user': os.getenv('METEO_DB_USER', 'default_user'),
    'password': os.getenv('METEO_DB_PASSWORD', 'default_password'),
    'database': os.getenv('METEO_DB_NAME', 'default_db')
}

DEBUG = os.getenv('DEBUG', 'True') == 'True'
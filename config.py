import os
import secrets
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        SECRET_KEY = secrets.token_hex(24)
        with open('secret_key.txt', 'w') as f:
            f.write(SECRET_KEY)

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mariadb+pymysql://angelo:angelo@localhost/passmana'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

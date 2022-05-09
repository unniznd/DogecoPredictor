
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = ['dogecopredictor.herokuapp.com']

SECRET_KEY = os.environ.get('SECRET_KEY')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
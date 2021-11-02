import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'f4cuk(!pf)_@o1fkqk$5(h85nzq@%voh_hc02*_35eo_rppf=x')

APPENV = os.getenv('DJANGO_APP_ENV', "LOCAL")

DEBUG = bool(int(os.getenv("DJANGO_DEBUG", 0)))

ROOT_URLCONF = 'config.urls'

ASGI_APPLICATION = 'config.asgi.application'

WSGI_APPLICATION = 'config.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

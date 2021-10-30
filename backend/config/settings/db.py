import os

from .vars import BASE_DIR

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DJANGO_DEFAULT_DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DJANGO_DEFAULT_DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.getenv("DJANGO_DEFAULT_DB_USER", "user"),
        "PASSWORD": os.getenv("DJANGO_DEFAULT_DB_PASSWORD", "password"),
        "HOST": os.getenv("DJANGO_DEFAULT_DB_HOST", "localhost"),
        "PORT": os.getenv("DJANGO_DEFAULT_DB_PORT", "5432"),
    }
}

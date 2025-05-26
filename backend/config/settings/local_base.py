from .base import *


DEBUG = True

HOST = "http://localhost:8000"

SECRET_KEY = "secret"  # noqa: S105

# STATIC_ROOT is NOT used during development (if DEBUG=True) 
# but it may be usefull if, for some reason, you want to run collectstatic on development
STATIC_ROOT = BASE_DIR.parent / "static"
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR.parent / "media"
MEDIA_URL = "/media/"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

AUTH_PASSWORD_VALIDATORS = []  # allow easy passwords only on local

# Email settings for mailhog
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mailhog"
EMAIL_PORT = 1025

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
    },
    "formatters": {
        "standard": {
            "format": "%(levelname)-8s [%(asctime)s] %(name)s: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {"handlers": ["console"], "level": "INFO"},
        "celery": {"handlers": ["console"], "level": "INFO"},
    },
}

JS_REVERSE_JS_MINIFY = False

from .base import *


SECRET_KEY = "test"  # nosec

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

# Speed up password hashing
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# import sentry_sdk
from decouple import Csv, config
# from sentry_sdk.integrations.django import DjangoIntegration

from .base import *


DEBUG = False

SECRET_KEY = config("SECRET_KEY")

DATABASES["default"]["ATOMIC_REQUESTS"] = True

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# STATIC_ROOT:
# - is unused during development (if DEBUG=True) 
# - is the destination for collectstatic
# - Nginx or WhiteNoise will serve static files from here
STATIC_ROOT = BASE_DIR.parent / "static"
STATIC_URL = "/static/"

# MEDIA_ROOT:
# - is the destination for user uploaded files
# - Nginx may serve media files from here
MEDIA_ROOT = BASE_DIR.parent / "media"
MEDIA_URL = "/media/"

# SERVER_EMAIL = "foo@example.com"

# EMAIL_HOST = "smtp.sendgrid.net"
# EMAIL_HOST_USER = config("SENDGRID_USERNAME")
# EMAIL_HOST_PASSWORD = config("SENDGRID_PASSWORD")
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# Security
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = False # Must be DISABLED!!! SSL redirect is enabled on Nginx.
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", default=3600, cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"


# Whitenoise
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

LOG_REQUESTS = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
    },
    "formatters": {
        "standard": {
            "format": "%(levelname)-8s [%(asctime)s] %(name)s: %(message)s"
        },
    },
    "handlers": {
        "null": {
            "class": "logging.NullHandler",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "filters": [],
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {"handlers": ["console"], "level": "INFO"},
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

JS_REVERSE_EXCLUDE_NAMESPACES = ["admin"]

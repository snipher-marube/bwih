from .base import *
from decouple import config
import cloudinary

DEBUG = False

ALLOWED_HOSTS = ['']

# Database configuration remains the same
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('NEON_DATABASE_NAME'),
        'USER': config('NEON_DATABASE_USER'),
        'PASSWORD': config('NEON_DATABASE_PASSWORD'),
        'HOST': config('NEON_DATABASE_HOST'),
        'PORT': config('NEON_DATABASE_PORT'),
        'CONN_MAX_AGE': 600,
        'OPTIONS': {
            'sslmode': 'require',
            'client_encoding': 'UTF8',
        }
    }
}

# Security settings (keep these)
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Domain and CORS settings 
DOMAIN = ""
CSRF_TRUSTED_ORIGINS = ['']


# cloudinary settings
cloudinary.config(
    cloud_name=config('CLOUDINARY_CLOUD_NAME'),
    api_key=config('CLOUDINARY_API_KEY'),
    api_secret=config('CLOUDINARY_API_SECRET'),
    secure=True
)

# default file storage
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
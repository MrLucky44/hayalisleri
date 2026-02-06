# Hayal İşleri - Production Settings for PythonAnywhere
# Copy relevant sections to your settings.py or create a separate production_settings.py

import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Update this with your actual secret key in production
# Generate a new secret key: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'CHANGE-THIS-TO-A-REAL-SECRET-KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Update with your PythonAnywhere domain and any custom domains
ALLOWED_HOSTS = [
    'YOUR_USERNAME.pythonanywhere.com',
    'www.hayalisleri.com',
    'hayalisleri.com',
]

# Update CSRF trusted origins for your domain
CSRF_TRUSTED_ORIGINS = [
    'https://YOUR_USERNAME.pythonanywhere.com',
    'https://www.hayalisleri.com',
]

# Database
# For MySQL on PythonAnywhere (recommended)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'YOUR_USERNAME$hayalisleri',
        'USER': 'YOUR_USERNAME',
        'PASSWORD': 'your-mysql-password',
        'HOST': 'YOUR_USERNAME.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# For SQLite (simpler, but not recommended for production)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings for production
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS
SESSION_COOKIE_SECURE = True  # Only send session cookie over HTTPS
CSRF_COOKIE_SECURE = True  # Only send CSRF cookie over HTTPS
SECURE_BROWSER_XSS_FILTER = True  # Enable browser XSS filter
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME sniffing
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking

# Optional: Email configuration for password resets, etc.
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@gmail.com'
# EMAIL_HOST_PASSWORD = 'your-app-password'
# DEFAULT_FROM_EMAIL = 'hayalisleri34@gmail.com'

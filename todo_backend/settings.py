from pathlib import Path
import os
import dj_database_url

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False").lower() == "True"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOST").split(" ") # Change to specific domains in production

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'corsheaders',
    'rest_framework',  # For REST APIs

    # Local apps
    'todos',  # Your app
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be first for CORS headers
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add Whitenoise middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todo_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'todo_backend.wsgi.application'

# Database configuration (SQLite for development)
DATABASES = {
    "default": dj_database_url.parse(
        os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3")  # Fallback to SQLite if not set
    )
}

DATABASES['default'] = dj_database_url.parse(os.environ.get("DATABASE_URL", ""))
database_url = os.environ.get("DATABASE_URL")

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Static files will be stored in this directory in production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Use Whitenoise to serve static files in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "https://bling011.github.io",  # Allow GitHub Pages frontend
    "https://todo-app-backend-oo2b.onrender.com",  # Allow your deployed backend
]

# Allow GitHub Pages and backend API server to bypass CSRF protection
CSRF_TRUSTED_ORIGINS = [
    "https://bling011.github.io",
    "https://todo-app-backend-oo2b.onrender.com",
]

# Enable CORS for specific methods (optional, useful for security)
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

# Allow credentials if needed (e.g., for authentication)
CORS_ALLOW_CREDENTIALS = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#postgres: postgresql://todo_app_backend_d2wy_user:S0vK6ftW0GBtuWP4Ig2mhfkZgqJoZdI1@dpg-cvnqk7vgi27c7383p5e0-a.oregon-postgres.render.com/todo_app_backend_d2wy
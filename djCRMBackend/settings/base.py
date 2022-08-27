"""
Django settings for djCRMBackend project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

import environ

env = environ.Env(DEBUG=(bool, False))  # set casting, default value

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")
# DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(",")
# ALLOWED_HOSTS = env(
#     "ALLOWED_HOSTS", cast=lambda hosts: [host.strip() for host in hosts.split(",")]
# )
ALLOWED_HOSTS = ["localhost","127.0.0.1"]


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

SITE_ID = 1

THIRD_PARTY_APPS = [
    "jazzmin",
    "rest_framework",
    "djoser",
    "rest_framework_simplejwt",
    "corsheaders",
    "django_filters",
]

LOCAL_APPS = [
    "apps.accounts",
    "apps.common",
    "apps.profiles",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "djCRMBackend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "djCRMBackend.wsgi.application"

# Django Database Backup Settings
# DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
# DBBACKUP_STORAGE_OPTIONS = {"location": BASE_DIR / "db_backup"}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# if DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }
# else:
#     DATABASES = {
#         "default": {
#             "ENGINE": env("POSTGRES_ENGINE"),
#             "NAME": env("POSTGRES_DB"),
#             "USER": env("POSTGRES_USER"),
#             "PASSWORD": env("POSTGRES_PASSWORD"),
#             "HOST": env("POSTGRES_DB_HOST"),
#             "PORT": env("POSTGRES_DB_PORT"),
#         }
#     }

# Parse database connection url strings
# like psql://user:pass@127.0.0.1:8458/db
# DATABASES = {
#     # read os.environ['DATABASE_URL'] and raises
#     # ImproperlyConfigured exception if not found
#     #
#     # The db() method is an alias for db_url().
#     'default': env.db(),

#     # read os.environ['SQLITE_URL']
#     'extra': env.db_url(
#         'SQLITE_URL',
#         default='sqlite:////tmp/my-tmp-sqlite.db'
#     )
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIR = []
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.User"



JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Yantrayug Adminstration",
    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Yantrayug Admin",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "logo/YantrayugLogo.png",
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    # Welcome text on the login screen
    "welcome_sign": "Welcome to the Yantrayug",
    # Copyright on the footer
    "copyright": "Yantrayug Hero Hub",
    # Field name on user model that contains avatar image
    "user_avatar": None,
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    # "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    "order_with_respect_to": ["user"],
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    # <i class="fas fa-globe-europe"></i>
    "icons": {
        # Auth
        "account.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "home.CircuitPackage": "fas fa-box-open",
        # Home
        # "home.Comment": "fas fa-comments",
        # "home.Continent": "fas fa-globe-europe",
        # "home.Country": "fas fa-flag",
        # "home.EveryYantrayugInclude": "fa fa-wrench",
        # "home.Offer": "fa fa-gift",
        # "home.PropertyAddOn": "fas fa-plus",
        # "home.PropertyRules": "fa fa-gavel",
        # "home.PropertyImages": "fas fa-image",
        # "home.Property": "fa fa-home",
        # "home.PropertyBooking": "fas fa-pen",
        # "home.PropertyExperience": "fas fa-user-tie",
        # "home.State": "fas fa-globe-africa",
        # "home.StateExtraInfo": "fas fa-city",
        # "home.YantrayugHomeExperience": "fas fa-user-tie",
        # "home.Tag": "fas fa-tag",
        # Portal
        # "portal.Address": "fas fa-address-card",
        # "portal.ContactInfo": "fas fa-file-signature",
        # "portal.FAQ": "fa fa-question-circle",
        # "portal.Investor": "fas fa-comment-dollar",
        # "portal.Page": "far fa-file",
        # "portal.PrivacyPolicy": "fas fa-lock",
        # "portal.SocialLink": "fa fa-link",
        # "portal.SubscribeNewsLetter": "fa fa-rocket",
        # "portal.Team": "fas fa-users-cog",
        # "portal.TermsCondition": "fa fa-gavel",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-globe-europe",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "horizontal_tabs",
        "auth.group": "horizontal_tabs",
    },
    # how many objects show er page
    "list_per_page": env("LIST_PER_PAGE", cast=int, default=20),
}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": False,
    # "accent": "accent-lime",
    # "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    # "sidebar": "sidebar-dark-primary",
    # "sidebar_nav_small_text": False,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    # "theme": "solar",
    # "dark_mode_theme": "darkly",
    # "button_classes": {
    #     "primary": "btn-primary",
    #     "secondary": "btn-secondary",
    #     "info": "btn-outline-info",
    #     "warning": "btn-outline-warning",
    #     "danger": "btn-outline-danger",
    #     "success": "btn-outline-success"
    # },
    "actions_sticky_top": True,
}




REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": (
        "Bearer",
        "JWT",
    ),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    # 'ROTATE_REFRESH_TOKENS': False,
    # 'BLACKLIST_AFTER_ROTATION': False,
    "SIGNING_KEY": env("SIGNING_KEY"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}


DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {
        # 'user_registration': 'apps.accounts.serializers.UserRegistrationSerializer',
        "user_create": "apps.accounts.serializers.CreateUserSerializer",
        "user": "apps.accounts.serializers.UserSerializer",
        "current_user": "apps.accounts.serializers.UserSerializer",
        # "current_user": "apps.profiles.serializers.ProfileSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
        # 'activation': 'djoser.serializers.ActivationSerializer',
        # 'login': 'djoser.serializers.LoginSerializer',
        # 'password_reset': 'djoser.serializers.PasswordResetSerializer',
        # 'password_reset_confirm':     'djoser.serializers.PasswordResetConfirmSerializer',
        # 'password_reset_confirm_retype': 'djoser.serializers.PasswordResetConfirmRetypeSerializer',
        # 'set_password': 'djoser.serializers.SetPasswordSerializer',
        # 'set_password_retype': 'djoser.serializers.SetPasswordRetypeSerializer',
        # 'set_username': 'djoser.serializers.SetUsernameSerializer',
        # 'set_username_retype': 'djoser.serializers.SetUsernameRetypeSerializer',
        # 'user_registration': 'djoser.serializers.UserRegistrationSerializer',
        # 'user': 'djoser.serializers.UserSerializer',
        # 'token': 'djoser.serializers.TokenSerializer',
    },
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_FROM = env("EMAIL_FROM")

PASSWORD_RESET_TOKEN_EXPIRE_MINUTES: int = 180
USER_SIGNUP_TOKEN_EXPIRE_MINUTES: int = 180


OTP = {
    "OTP_DIGIT_LENGTH": env("OTP_DIGIT_LENGTH", cast=int, default=6),
    "OTP_EXPIRATION_TIME": timedelta(
        minutes=env("OTP_EXPIRATION_TIME_IN_MINUTES", cast=int, default=30),
        seconds=env("OTP_EXPIRATION_TIME_IN_SECONDS", cast=int, default=0),
    ),
}


# twiilio sms sending API
SMS = {
    "account_sid": env("account_sid"),
    "auth_token": env("auth_token"),
    "from_number": env("from_number"),
}


# Razorpay settings
# RAZORPAY_KEY_ID = config("RAZORPAY_TEST_KEY_ID")
# RAZORPAY_KEY_SECRET = config("RAZORPAY_TEST_KEY_SECRET")
if DEBUG:
    RAZORPAY_KEY_ID = env("RAZORPAY_TEST_KEY_ID")
    RAZORPAY_KEY_SECRET = env("RAZORPAY_TEST_KEY_SECRET")
else:
    RAZORPAY_KEY_ID = env("RAZORPAY_LIVE_KEY_ID")
    RAZORPAY_KEY_SECRET = env("RAZORPAY_LIVE_KEY_SECRET")

RAZORPAY_WEBHOOK_KEY_SECRET = env("RAZORPAY_WEBHOOK_KEY_SECRET")

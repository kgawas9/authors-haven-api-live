from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
        'DJANGO_SECRET_KEY', 
        default="django-insecure-2i61g63!j-3nt3jpblq7+zc0@tzy2d#y^j6p%op3++!4rt$!gs",
    )

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

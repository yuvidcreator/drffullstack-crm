from __future__ import absolute_import
import os

from celery import Celery
from djCRMBackend.settings import base



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djCRMBackend.settings.development")

app = Celery("djCRMBackend")

app.config_from_object("djCRMBackend.settings.development", namespace="CELERY")

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
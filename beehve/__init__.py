from __future__ import absolute_import
__version__ = "1.0.2"

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

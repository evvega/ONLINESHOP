from django.apps import apps
from django.contrib import admin

from .models import *

# auto-register all models

app = apps.get_app_config('store')

for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

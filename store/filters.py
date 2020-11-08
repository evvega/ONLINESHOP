# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters

from .models import *


class TutorialFilter(filters.FilterSet):
    class Meta:
        model = Tutorial
        fields = ['title']

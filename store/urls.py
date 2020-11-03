
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.routers import DefaultRouter

from .api_views import *

router = DefaultRouter()
router.register(r'tutorials', TutorialViewSet, 'tutorial')


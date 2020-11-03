"""ONLINESHOP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import include, url

import store
from ONLINESHOP import settings
from common.views import health_check

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('djoser.urls.base')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^health_check/', health_check),
]


# Swagger URLs
schema_view = get_swagger_view(title='API',)
urlpatterns.extend([
    url(r'^api/docs/$', schema_view)
])

for core_module in settings.APP_MODULES:
    module = __import__(core_module, globals(), locals(), ['urls'], 0)
    urls = module.urls
    urlpatterns.append(url(r'^{0}/'.format(core_module), include(urls.router.urls)))


# DRF URLs
urlpatterns.extend([
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
])
"""crypto_bear_bucks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from wallet import views
from cc import urls

# api routing
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Vanity headers / titles for admin page
admin.site.site_header = 'Crypto Bear Bucks Admin'
admin.site.site_title = 'My site admin'
admin.site.index_title = 'Site administration'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^wallet/', include('wallet.urls')),
    url(r'^cc/', include('cc.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
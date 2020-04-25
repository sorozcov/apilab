"""example URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)

from babies.views import BabyViewSet
from parents.views import ParentViewSet
from events.views import EventViewSet

router = routers.DefaultRouter()

router.register(r'babies', BabyViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'events', EventViewSet)
#api/babies
#api/parents
#api/events

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/token-auth/', obtain_jwt_token),
    url(r'^api/v1/token-refresh/', refresh_jwt_token),
]

#  Para realizar login y autenticacion como parent
#  \url(r'^api/v1/token-auth/', obtain_jwt_token),
#  url(r'^api/v1/token-refresh/', refresh_jwt_token),


#Para realizar todas las acciones necesarias del api
#api/babies
#api/parents
#api/events
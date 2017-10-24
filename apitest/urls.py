from django.conf.urls import url,include
from rest_framework import routers
from apitest import views

router = routers.DefaultRouter()
router.register(r'^users', views.UserViewSet)

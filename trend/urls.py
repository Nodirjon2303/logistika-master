from django.urls import path
from .views import *
urlpatterns=[
    path('trend/',TrendPageView,name='trend'),
]
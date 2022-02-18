from django.urls import path
from .views import *
urlpatterns=[
    path('',CalculatorPageView,name='calculator'),
    path('company/',CompanySendFunc),
    path('saqlash/',Saqlash),


]
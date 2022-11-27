from django.urls import path
from .views import home,index,test

urlpatterns= [
    path('', home,name="home"),
    path('index', index,name="index"),
    path('test', test,name="test"),
]
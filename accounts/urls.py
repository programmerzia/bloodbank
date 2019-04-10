from django.urls import path
from . import views as user_view

urlpatterns = [
    path('',user_view.home,name="home"),
]
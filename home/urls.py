from django.urls import path
from home import views

urlpatterns = [
	path('', views.home, name="home"),
	path('search_donor', views.search_donor, name="search_donor"),
]
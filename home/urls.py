from django.urls import path
from home import views

app_name = 'main_site'
urlpatterns = [
	path('', views.home, name="home"),
	path('search_donor', views.search_donor, name="search_donor"),
	path('contact', views.contact, name='contact'),
	path('thankyou', views.thank_you, name='thank-you'),
	path('register',views.register, name='register'),
	path('registration_success',views.registration_success, name='registration_success')
]
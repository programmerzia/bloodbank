from django.urls import path
from . import views as user_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', user_view.dashboard, name="dashboard"),
    path('profile', user_view.profile, name="profile"),
    path('login', auth_view.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('register', user_view.register, name="register"),
    path('password_change', auth_view.PasswordChangeView.as_view(template_name="accounts/password_change.html")),
    path('password_chage/done', auth_view.PasswordChangeDoneView.as_view(template_name="password_change_done.html")),

]
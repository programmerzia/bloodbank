from django.urls import path
from accounts import views as user_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', user_view.dashboard, name="dashboard"),
    path('profile/', user_view.profile, name="profile"),
    path('login/', auth_view.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('login/', auth_view.LoginView.as_view(template_name="accounts/login.html"), name="logout"),
    path('register/', user_view.register, name="register"),
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name="accounts/password_change.html"), name="password_change"),
    path('password_chage/done/', auth_view.PasswordChangeDoneView.as_view(template_name="password_change_done.html"), name="password_change_done"),
    path('add_user/', user_view.add_user, name="add_user"),
    path('list_user/', user_view.list_user, name="list_user"),
    path('add_member/', user_view.add_member, name="add_member"),
    path('list_member/', user_view.list_member, name="list_member"),
]
from django.urls import path
from . import views
urlpatterns = [
    path('add_data', views.add_data, name="add_data"),
    path('data_list',views.data_list, name="data_list"),
    path('edit_data/<int:pk>', views.edit_data, name="edit_data"),
    path('delete_data/<int:pk>', views.delete_data, name="delete_data"),
]
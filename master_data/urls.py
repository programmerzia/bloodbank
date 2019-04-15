from django.urls import path
from . import views
urlpatterns = [
	path('',views.option,name='master_data'),
    path('add_data', views.add_data, name="add_data"),
    path('data_list',views.data_list, name="data_list"),
    path('edit_data/<int:pk>', views.edit_data, name="edit_data"),
    path('delete_data/<int:pk>', views.delete_data, name="delete_data"),
    path('option', views.option, name="option"),
    path('edit_option', views.edit_option, name="edit_option"),
    path('delete_option/<int:pk>', views.delete_data, name="delete_option"),
]
from django.urls import path
from . import views



urlpatterns = [
    path('', views.files_index, name='files_index'),
]
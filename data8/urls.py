from django.urls import path
from . import views

urlpatterns = [
    path('modelform/', views.db_open_model_form_way, name='model_form'),
    path('', views.db_open_model_form_way, name='model_form'),
    
]

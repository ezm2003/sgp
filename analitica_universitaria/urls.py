
from django.urls import path
from . import views

app_name = 'app_analitica_universitaria'

urlpatterns = [
    path('analitica_universitaria/', views.analitica_universitaria, name='analitica_universitaria'), 
    path('analitica_universitaria/prorrateo', views.prorrateo, name='prorrateo'), 


]

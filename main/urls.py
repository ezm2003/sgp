from django.urls import path
from . import views

app_name = 'main'  # Agrega un namespace para la app

urlpatterns = [
    path('home/', views.home, name='home'),
    path('hope_ui/', views.hope_ui, name='hope_ui'),
    path('base/', views.base, name='base'),

]


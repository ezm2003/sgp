from django.urls import path
from . import views

app_name = 'app_login'  

urlpatterns = [
    #login
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout'),

    #User
    path('user_profile/', views.user_profile, name='user_profile'),

]
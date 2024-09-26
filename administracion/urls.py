from django.urls import path
from . import views

app_name = 'app_administracion' 

urlpatterns = [
    path('user_list/', views.user_list, name='user_list'),
    path('user_manage/', views.user_manage, name='user_manage'),
    path('user_edit_role/', views.user_edit_role, name='user_edit_role'),

]

from django.urls import path
from . import views

app_name = 'app_proyectos'

urlpatterns = [
    path('crud_projects/', views.crud_projects, name='crud_projects'),  # Nota el uso de '/' al final para ser consistente
    path('crud_projects/create_projects/', views.create_projects, name='create_projects'),  # URL para crear proyectos sin ID
    path('crud_projects/create_projects/<int:project_id>/', views.create_projects, name='create_projects_with_id'),  # URL para crear proyectos con ID

    path('state_projects/', views.state_projects, name='state_projects'),  # Nota el uso de '/' al final para ser consistente

]

"""
from django.urls import path
from . import views

app_name = 'app_proyectos'  

urlpatterns = [
    path('crud_projects', views.crud_projects, name='crud_projects'),
    path('crud_projects/create_projects', views.create_projects, name='create_projects'),
    path('crud_projects/create_projects/<int:project_id>/', views.create_projects, name='create_projects'),

]
"""
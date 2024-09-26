from django.shortcuts import render, redirect
from .decorators import *
import requests
from django.conf import settings
import json
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from main.models import APIClient



@login_required_custom
def base(request):

    return render(request, 'base.html')


@login_required_custom
def home(request):
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])

    totals = {}
    totals['total_proyectos'] = get_total("proyecto")
    totals['total_hitos'] = get_total("hito")
    totals['total_actividades'] = get_total("actividad")

    return render(request, 'home.html', {
        'user_avatar': user_avatar,
        'user_name': user_name,
        'user_lastname': user_lastname,
        'user_roles': user_roles,
        'totals': totals  # Pasar el diccionario al contexto

    })

def get_total(entity):
        client = APIClient(entity)
        data = client.get_data()
        return len(data)
    



@login_required_custom
def hope_ui(request):
    return render(request, 'hope_ui.html')




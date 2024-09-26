from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.contrib.auth.models import User

from django.urls import reverse
from django.http import JsonResponse

import requests

from django.conf import settings

from django.contrib import messages

from .models import *
from .exceptions import AuthenticationError, APIConnectionError, UserNotFoundError


def inicio(request):
    return render(request,'inicio.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Usuario.authenticate(email, password)
            if not user:
                raise AuthenticationError("Correo electrónico o contraseña inválidos.")

            persona = Usuario.get_persona_data(email)
            if not persona:
                raise UserNotFoundError("No se encontraron datos de perfil para el usuario.")
            
            app_id = 4  # ID del aplicativo "Sistema de Gestión de Proyectos"
            if not Usuario.check_user_access(email, app_id):
                raise UserNotFoundError("El usuario no tiene acceso al aplicativo.")
            

            user_roles = Usuario.get_user_roles(email, app_id)


            # Guardar datos en la sesión
            request.session['user_email'] = user['email']
            request.session['user_name'] = persona.get('nombre', '')
            request.session['user_lastname'] = persona.get('apellidos', '')
            request.session['user_avatar'] = persona.get('avatar', '')
            request.session['user_roles'] = user_roles  # Guardar los roles en la sesión

            return redirect('main:home')

        except AuthenticationError as e:
            return render(request, 'login.html', {'error_message': str(e)})

        except UserNotFoundError as e:
            return render(request, 'login.html', {'error_message': str(e)})

        except APIConnectionError:
            return render(request, 'login.html', {'error_message': "Error al conectar con el servicio de autenticación."})

    return render(request, 'login.html')



def logout(request):    
    request.session.flush()
    return redirect('app_login:login_view') 


def user_profile(request):
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])


    return render(request, 'user_profile.html', {
        'user_avatar': user_avatar,
        'user_name': user_name,
        'user_lastname': user_lastname,
        'user_roles': user_roles  
    })

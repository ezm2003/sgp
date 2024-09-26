# your_project/your_auth_backend.py

import requests
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.conf import settings


class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        api_url = f"{settings.API_URL}usuario"
        


        request_body = {
            "procedure": "select_json_entity",
            "parameters": {
                "table_name": "usuario",
                "where_condition": "email = %(email)s",
                "json_data": {
                    "email": username
                },
                "select_columns": "email, contrasena"
            }
        }
        response = requests.get(api_url, json=request_body)
        api_url = f"{settings.API_URL}usuario"
        print(f"API URL: {api_url}")  # Agrega esta línea para verificar la URL
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")
        if response.status_code == 200:
            data = response.json()
            if data and data[0]['contrasena'] == password:
                return User.objects.get_or_create(username=username)[0]
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None











"""# login/backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Usuario  # Asegúrate de importar tu modelo personalizado

class UsuarioBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Usuario.objects.get(email=username)
            if user.contrasena == password:  # Asegúrate de usar una comparación segura
                return user
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None



from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import connection

class CustomBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, email, contrasena FROM usuario WHERE email = %s",
                [email]
            )
            user = cursor.fetchone()
        
        if user and user[2] == password:
            UserModel = get_user_model()
            try:
                user_obj = UserModel.objects.get(pk=user[0])
            except UserModel.DoesNotExist:
                user_obj = UserModel(pk=user[0], username=email, email=email)
            return user_obj

        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
"""
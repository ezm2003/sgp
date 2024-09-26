import requests
from django.conf import settings
import json

class Usuario:
    @staticmethod
    def authenticate(email, password):
        api_url = f"{settings.API_URL}"
        payload = {
            "procedure": "select_json_entity",
            "parameters": {
                "table_name": "usuario",
                "select_columns": "email, contrasena",
                "where_condition": f"email = '{email}'"
            }
        }
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            users = response.json()
            user = users['outputParams']['result'][0] if users['outputParams']['result'] else None
            if user and password == user['contrasena']:
                return user  # Devuelve el usuario sin verificar el acceso
        return None


    
    @staticmethod
    def check_user_access(email, app_id):
        api_url = f"{settings.API_URL}"
        permission_payload = {
            "procedure": "select_json_entity",
            "parameters": {
                "table_name": "rol_usuario_aplicacion",
                "select_columns": "fk_aplicacion",
                "where_condition": f"fk_usuario = '{email}' AND fk_aplicacion = {app_id}"
            }
        }
        response = requests.post(api_url, json=permission_payload)
        if response.status_code == 200:
            permissions = response.json()
            return bool(permissions['outputParams']['result'])
        return False
    


    @staticmethod
    def get_persona_data(email):
        api_url = f"{settings.API_URL}"
        persona_payload = {
            "procedure": "select_json_entity",
            "parameters": {
                "table_name": "persona",
                "select_columns": "nombre, apellidos, avatar",
                "where_condition": f"email = '{email}'"
            }
        }
        persona_response = requests.post(api_url, json=persona_payload)
        if persona_response.status_code == 200:
            personas = persona_response.json()
            persona = personas['outputParams']['result'][0] if personas['outputParams']['result'] else None
            return persona
        return None


    @staticmethod
    def get_user_roles(email, app_id):
        api_url = f"{settings.API_URL}"
        role_payload = {
            "procedure": "select_json_entity",
            "parameters": {
                "table_name": "rol_usuario_aplicacion",
                "select_columns": "fk_aplicacion",
                "where_condition": f"fk_usuario = '{email}' AND fk_aplicacion = {app_id}"
            }
        }
        response = requests.post(api_url, json=role_payload)
        
        if response.status_code == 200 and response.content:
            try:
                role_data = response.json()

                # Verifica si hay un campo 'result' en la respuesta
                if role_data.get('result'):
                    # Deserializa el JSON anidado en el primer 'result'
                    nested_result_str = role_data['result'][0]['result']
                    nested_result = json.loads(nested_result_str)  # Convierte el string JSON a una lista/diccionario

                    # Extrae los roles de la lista anidada
                    return [
                        Usuario.get_role_name(role.get('fk_rol'))
                        for role in nested_result
                        if role.get('fk_aplicacion') == app_id
                    ]
            except (ValueError, KeyError) as e:
                # Manejar el error si el JSON no es válido o falta una clave
                print(f"Error procesando la respuesta JSON: {e}")
                return ['Sin rol asignado']

        return ['Sin rol asignado']
    

    @staticmethod
    def get_role_name(role_id):
        api_url = f"{settings.API_URL}"
        role_payload = {
            "procedure": "select_json_entity",
            "parameters": {
                "table_name": "rol",
                "select_columns": "nombre",
                "where_condition": f"id_rol = {role_id}"
            }
        }
        response = requests.post(api_url, json=role_payload)

        
        if response.status_code == 200:
            role_data = response.json()
            # Obtener el nombre del rol
            if role_data.get('result'):
                nested_result = role_data['result'][0].get('result', '[]')
                role_name = json.loads(nested_result)[0].get('nombre', 'Nombre de rol desconocido')
                return role_name
        return 'Nombre de rol desconocido'




"""
import requests
from django.conf import settings

class Usuario:
    @staticmethod
    def authenticate(email, password):
        api_url = f"{settings.API_URL}"
        payload = {
            "procedure": "select_json_entity",
            "parameters": {
                "table_name": "usuario",
                "select_columns": "email, contrasena",
                "where_condition": f"email = '{email}'"
            }
        }
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            users = response.json()
            user = users['outputParams']['result'][0] if users['outputParams']['result'] else None
            if user and password == user['contrasena']:
                return user
        return None

    @staticmethod
    def get_persona_data(email):
        api_url = f"{settings.API_URL}"
        persona_payload = {
            "procedure": "select_json_entity",
            "parameters": {
                "table_name": "persona",
                "select_columns": "nombre, apellidos, avatar",
                "where_condition": f"fk_email_usuario = '{email}'"
            }
        }
        persona_response = requests.post(api_url, json=persona_payload)
        if persona_response.status_code == 200:
            personas = persona_response.json()
            persona = personas['outputParams']['result'][0] if personas['outputParams']['result'] else None
            return persona
        return None

    @staticmethod
    def check_user_access(email, app_id):
        api_url = f"{settings.API_URL}"
        access_payload = {
            "procedure": "select_json_entity",
            "parameters": {
                "table_name": "usuariorolaplicacion",
                "select_columns": "fkemail",
                "where_condition": f"fkemail = '{email}' AND fkidaplicacion = {app_id}"
            }
        }

        response = requests.post(api_url, json=access_payload)
        if response.status_code == 200:
            access_data = response.json()
            access = access_data['outputParams']['result'] if access_data['outputParams']['result'] else None
            return bool(access)
        return False



    @staticmethod
    def get_user_role(email):
        api_url = f"{settings.API_URL}"
        role_payload = {
            "procedure": "select_json_entity",
            "parameters": {
                "table_name": "usuariorolaplicacion",
                "select_columns": "rol.nombre",
                "join": {
                    "table": "rol",
                    "on": "usuariorolaplicacion.fkidrol = rol.id"
                },
                "where_condition": f"fkemail = '{email}'"
            }
        }
        response = requests.post(api_url, json=role_payload)
        if response.status_code == 200:
            role_data = response.json()
            # Acceder a los datos correctamente
            roles = role_data.get('outputParams', {}).get('result', [])
            if roles:
                # Obtener el primer rol
                role = roles[0]  # Puede ser una lista con un solo rol
                # Retornar el nombre del rol si existe
                return role.get('nombre', 'Sin rol asignado')
        return 'Sin rol asignado'



import requests
from django.conf import settings
from .exceptions import AuthenticationError, APIConnectionError, UserNotFoundError


class Usuario:
    @staticmethod
    def authenticate(email, password):
        try:
            api_url = f"{settings.API_URL}"
            payload = {
                "procedure": "select_json_entity",
                "parameters": {
                    "table_name": "usuario",
                    "select_columns": "email, contrasena",
                    "where_condition": f"email = '{email}'"
                }
            }
            response = requests.post(api_url, json=payload)
            response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
            users = response.json()
            user = users['outputParams']['result'][0] if users['outputParams']['result'] else None
            
            if user and password == user['contrasena']:
                return user
            else:
                raise AuthenticationError("Correo electrónico o contraseña inválidos.")
        
        except requests.RequestException as e:
            raise APIConnectionError(f"Error de conexión con la API: {e}")

    @staticmethod
    def get_persona_data(email):
        try:
            api_url = f"{settings.API_URL}"
            persona_payload = {
                "procedure": "select_json_entity",
                "parameters": {
                    "table_name": "persona",
                    "select_columns": "nombre, apellidos, avatar",
                    "where_condition": f"fk_email_usuario = '{email}'"
                }
            }
            persona_response = requests.post(api_url, json=persona_payload)
            persona_response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
            personas = persona_response.json()
            persona = personas['outputParams']['result'][0] if personas['outputParams']['result'] else None
            
            if persona:
                return persona
            else:
                raise UserNotFoundError("Datos de la persona no encontrados.")
        
        except requests.RequestException as e:
            raise APIConnectionError(f"Error de conexión con la API: {e}")
"""
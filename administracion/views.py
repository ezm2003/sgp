from django.shortcuts import render,redirect
from main.decorators import *
import requests
from django.conf import settings
import json
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from main.models import APIClient
from django.http import JsonResponse
from django.contrib import messages


"""
@login_required_custom
def user_list(request):
    #data basic
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])
    
    #List users
    persona_data = APIClient('persona')
    users = persona_data.get_data()

    
    if request.method == "POST":
        action = request.POST.get('send')  # Obtén el valor del campo de acción
        user_email = request.POST.get('user_email')  # Obtén el correo del usuario a eliminar
        match action:

            case "user_manage":
                return redirect('app_administracion:user_manage')
            
            case "update_user":
                print("update USUARIO")

            case "delete_user":
                #Si no se encuentra el usuario desde el html
                if not user_email:
                    print("No se proporcionó un correo electrónico de usuario para eliminar")
                else:
                    #llama a la funcion delete_persona que a su vez llama al metodo delete_data
                    success_persona, error_message_persona = delete_persona(user_email)
                    if not success_persona:
                        print(f"Error al eliminar persona: {error_message_persona}")
                    else:
                        print("Persona eliminado exitosamente")

                    #Si la persona a sido eliminado correctamente eliminara al usuario
                    if success_persona:
                        success_usuario, error_message_usuario = delete_usuario(user_email)

                        if not success_usuario:
                            print(f"Error al eliminar usuario: {error_message_usuario}")
                        else:
                            print("Usuario eliminado exitosamente")
                            return redirect('app_administracion:user_list')
    

    return render(request, 'user_list.html', {
        'user_avatar': user_avatar,
        'user_name': user_name,
        'user_lastname': user_lastname,
        'user_roles': user_roles,
        "users": users,
    })
"""
@login_required_custom
def user_list(request):
    #data basic
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])
    
    #List users
    persona_data = APIClient('persona')
    users = persona_data.get_data()

    
    if request.method == "POST":
        action = request.POST.get('send')  # Obtén el valor del campo de acción
        user_email = request.POST.get('user_email')  # Obtén el correo del usuario a eliminar
        match action:

            case "user_manage":
                return redirect('app_administracion:user_manage')
            
            case "update_user":
                print("update USUARIO")

            case "delete_user":
                #Si no se encuentra el usuario desde el html
                if not user_email:
                    return JsonResponse({'success': False, 'message': 'No se proporcionó un correo electrónico de usuario para eliminar'})

                else:
                    #llama a la funcion delete_persona que a su vez llama al metodo delete_data
                    success_persona, error_message_persona = delete_persona(user_email)
                    
                    if not success_persona:
                        return JsonResponse({'success': False, 'message': error_message_persona})

                    #Si la persona a sido eliminado correctamente eliminara al usuario
                    if success_persona:
                        success_usuario, error_message_usuario = delete_usuario(user_email)

                        if not success_usuario:
                            return JsonResponse({'success': False, 'message': error_message_usuario})
                        else:
                            return JsonResponse({'success': True, 'message': 'Usuario eliminado exitosamente'})


    return render(request, 'user_list.html', {
        'user_avatar': user_avatar,
        'user_name': user_name,
        'user_lastname': user_lastname,
        'user_roles': user_roles,
        "users": users,
    })




def delete_usuario(user_email):
    try:
        usuario_client = APIClient('usuario')
        try:
            usuario_client.delete_data(where_condition=f"email = '{user_email}'")        
        except Exception as e:
            return False, f"Error al borrar usuario: {str(e)}"

        return True, None 

    except Exception as e:
        raise RuntimeError(f"Error del servidor: {str(e)}")

def delete_persona(user_email):
    try:
        persona_client = APIClient('persona')

        try:
            persona_client.delete_data(where_condition=f"fk_email_usuario = '{user_email}'")
        except Exception as e:
            return False, f"Error al borrar persona: {str(e)}"

        return True, None 

    except Exception as e:
        raise RuntimeError(f"Error del servidor: {str(e)}")


"""
def delete_user(user_email):
    try:
        # Crear instancias de APIClient para ambas tablas
        usuario_client = APIClient('usuario')
        persona_client = APIClient('persona')

        # Eliminar el usuario
        usuario_client.delete_data(where_condition=f"email = '{user_email}'")

        # Eliminar la persona asociada al usuario
        persona_client.delete_data(where_condition=f"fk_email_usuario = '{user_email}'")

        return True, None  # Indica éxito
    except Exception as e:
        return False, str(e)  # Indica error y devuelve el mensaje de error
"""

"""
@login_required_custom
def user_list(request):
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])

    api_client = APIClient('persona')
    users = api_client.get_data()

    return render(request, 'user_list.html', {
        'user_avatar': user_avatar,
        'user_name': user_name,
        'user_lastname': user_lastname,
        'user_roles': user_roles,

        "users":users 
    })
"""


@login_required_custom
def user_manage(request):
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])


    return render(request, 'user_manage.html', {
        'user_avatar': user_avatar,
        'user_name': user_name,
        'user_lastname': user_lastname,
        'user_roles': user_roles  
    })



@login_required_custom
def user_edit_role(request):
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])


    return render(request, 'user_edit_role.html', {
        'user_avatar': user_avatar,
        'user_name': user_name,
        'user_lastname': user_lastname,
        'user_roles': user_roles  
    })


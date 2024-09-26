from django.shortcuts import redirect
from functools import wraps
from django.shortcuts import render


def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_email' not in request.session:
            return redirect('app_login:login_view')
        return view_func(request, *args, **kwargs)
    
    return wrapper


"""
from django.http import HttpResponse
def user_data_views(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Obtén los datos del usuario de la sesión
        user_avatar = request.session.get('user_avatar', '')
        user_name = request.session.get('user_name', '')
        user_lastname = request.session.get('user_lastname', '')

        # Llama a la vista original
        response = view_func(request, *args, **kwargs)

        if isinstance(response, HttpResponse) and hasattr(response, 'content'):
            # Modificar la respuesta aquí puede ser complicado, así que asegúrate de
            # que `view_func` pase el contexto adecuadamente.
            return response

        return response

    return _wrapped_view
"""
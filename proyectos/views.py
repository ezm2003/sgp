from django.shortcuts import render,redirect
from main.decorators import login_required_custom
from main.models import APIClient
from django.views.decorators.http import require_POST
from django.utils import timezone


@login_required_custom
def crud_projects(request):
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])
    user_email = request.session.get('user_email', '')

    client = APIClient("proyecto")    


    if request.method == "POST":
        project_id = request.POST.get('project_id')
        action = request.POST.get('send')

        if action == "delete_project" and project_id:
            delete_project(request, user_email)
            return redirect('app_proyectos:crud_projects')  # Redirigir después de eliminar

    
    projects = client.get_data(where_condition=f"email_creador = '{user_email}'")


    return render(request, 'crud_projects.html', {
        'user_avatar': user_avatar,
        'user_name': user_name,
        'user_lastname': user_lastname,
        'user_roles': user_roles,
        'projects': projects,
    })








@login_required_custom
def create_projects(request, project_id=None):
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])
    user_email = request.session.get('user_email', '')

    action = request.POST.get('send')  # Obtén el valor del campo de acción
    
    client = APIClient("proyecto")
    user_projects = client.get_data(where_condition=f"email_creador = '{user_email}'")

    if project_id:
        project_data = consult_project(request, user_email)
        return render(request, 'create_projects.html', {
                'user_avatar': user_avatar,
                'user_name': user_name,
                'user_lastname': user_lastname,
                'user_roles': user_roles,
                'project': project_data,  
                'projects': user_projects  # Pasar proyectos al contexto

            })


    match action:
        case "project_save":
            save_project(request, user_email)
            return redirect('app_proyectos:crud_projects')  

        case "project_consult":
            project_data = consult_project(request, user_email)
            return render(request, 'create_projects.html', {
                'user_avatar': user_avatar,
                'user_name': user_name,
                'user_lastname': user_lastname,
                'user_roles': user_roles,
                'project': project_data,  
                'projects': user_projects  # Pasar proyectos al contexto


            })
        
        case "project_update":
            return update_project(request, user_email)
        
        case "project_delete":
            return delete_project(request, user_email)
        
        case "project_cancel":
            return redirect('app_proyectos:crud_projects')  
        

        

        case _:
            return render(request, 'create_projects.html', {
                'user_avatar': user_avatar,
                'user_name': user_name,
                'user_lastname': user_lastname,
                'user_roles': user_roles,
                'projects': user_projects  # Pasar proyectos al contexto

            })




def save_project(request, user_email):
    client = APIClient("proyecto")

    current_datetime = timezone.now().isoformat()  # '2024-09-03T20:12:55.670568'


    json_data = {
        "nombre": request.POST.get('project_name'),
        "descripcion": request.POST.get('project_description'),
        "fecha_inicio": request.POST.get('project_date_start'),
        "fecha_fin": request.POST.get('project_date_end'),
        "email_creador": user_email,
        "objetivo": request.POST.get('project_objetive'),
        "fecha_ultima_modificacion": current_datetime
    }
    print(json_data)

    client.insert_data(json_data=json_data)

def consult_project(request, user_email):
    project_id = request.POST.get('project_id')
    if not project_id:
        # Maneja el caso donde no se ha proporcionado un ID de proyecto
        return None

    client = APIClient("proyecto")
    json_data = {
        "id_proyecto": project_id
    }
    project_data = client.get_data(
        where_condition=f"id_proyecto = '{project_id}'",
        select_columns="id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin, email_creador, objetivo",
        json_data=json_data
    )
    
    # Devolver el primer resultado si hay datos, o None si no se encontró ningún proyecto
    return project_data[0] if project_data else None



def update_project(request, user_email):
    client = APIClient("proyecto")

    project_id = request.POST.get('project_id')  # Suponiendo que el ID del proyecto se envía

    current_datetime = timezone.now().isoformat()  # '2024-09-03T20:12:55.670568'


    json_data = {
        "nombre": request.POST.get('project_name'),
        "descripcion": request.POST.get('project_description'),
        "fecha_inicio": request.POST.get('project_date_start'),
        "fecha_fin": request.POST.get('project_date_end'),
        "objetivo": request.POST.get('project_objetive'),
        "fecha_ultima_modificacion": current_datetime

    }
    where_condition = f"id_proyecto = {project_id}"
    client.update_data(where_condition=where_condition, json_data=json_data)
    return redirect('app_proyectos:crud_projects')  # Redirige a la lista de proyectos




def delete_project(request, user_email):
    client = APIClient("proyecto")
    project_id = request.POST.get('project_id')  # Suponiendo que el ID del proyecto se envía
    where_condition = f"id_proyecto = {project_id}"
    client.delete_data(where_condition=where_condition)
    return redirect('app_proyectos:crud_projects')  # Redirige a la lista de proyectos







@login_required_custom
def state_projects(request):
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])
    user_email = request.session.get('user_email', '')

    client = APIClient("proyecto")    
    projects = client.get_data()


    return render(request, 'state_projects.html', {
        'user_avatar': user_avatar,
        'user_name': user_name,
        'user_lastname': user_lastname,
        'user_roles': user_roles,
        'projects': projects,
    })

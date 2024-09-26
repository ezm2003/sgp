from django.shortcuts import render, redirect
from django.db import connection
import plotly.express as px
import plotly.io as pio
import pandas as pd
from django.http import HttpResponse
from main.decorators import login_required_custom
from django.utils.safestring import mark_safe




@login_required_custom
def analitica_universitaria(request):
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])
    user_email = request.session.get('user_email', '')




    return render(request, 'analitica_universitaria.html', {
        'user_avatar': user_avatar,
        'user_name': user_name,
        'user_lastname': user_lastname,
        'user_roles': user_roles,
    })


"""
@login_required_custom
def prorrateo(request):
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])
    user_email = request.session.get('user_email', '')

    if request.method == 'POST':
        profesor_seleccionado = request.POST.get('profesor')

        # Ejecutar consulta SQL
        with connection.cursor() as cursor:
            query = 
                SELECT ins.nombre AS nombre_x, pa.nombre AS nombre_y, ins.prog_acad AS programa
                FROM inscripciones ins
                JOIN programacion_academica pa ON pa.n_clase = ins.n_clase
                WHERE pa.nombre = %s
            
            cursor.execute(query, [profesor_seleccionado])
            rows = cursor.fetchall()

        # Convertir los resultados a un DataFrame de pandas
        df = pd.DataFrame(rows, columns=['nombre_x', 'nombre_y', 'programa'])

        # Agrupar los datos por profesor y programa y contar los estudiantes únicos
        df_grouped = df.groupby(['nombre_y', 'programa'])['nombre_x'].nunique().reset_index()
        df_grouped = df_grouped.rename(columns={'nombre_x': 'num_estudiantes'})

        # Calcular el número total de estudiantes por profesor
        total_students_per_professor = df_grouped.groupby('nombre_y')['num_estudiantes'].sum()

        # Calcular el porcentaje de estudiantes por programa para cada profesor
        df_grouped['percentage'] = df_grouped.apply(lambda row: row['num_estudiantes'] / total_students_per_professor[row['nombre_y']] * 100, axis=1)

        # Extraer los datos para el profesor deseado
        data_profesor = df_grouped[df_grouped['nombre_y'] == profesor_seleccionado]

        # Crear el gráfico
        fig = px.pie(data_profesor, values='percentage', names='programa', title=profesor_seleccionado,
                     hover_data=['num_estudiantes'], labels={'num_estudiantes':'Número de estudiantes'})
        
        # Convertir el gráfico a HTML
        graph_html = pio.to_html(fig, full_html=False)
        return render(request, 'prorrateo.html', {
            'user_avatar': user_avatar,
            'user_name': user_name,
            'user_lastname': user_lastname,
            'user_roles': user_roles,
            'graph_html': mark_safe(graph_html),
            'profesores': get_profesores()  # Asegúrate de definir esta función para obtener la lista de profesores
        })

    else:
        # Para GET, simplemente mostrar la página con el formulario
        return render(request, 'prorrateo.html', {
            'user_avatar': user_avatar,
            'user_name': user_name,
            'user_lastname': user_lastname,
            'user_roles': user_roles,
            'graph_html': '',  # No mostrar gráfico al principio
            'profesores': get_profesores()  # Asegúrate de definir esta función para obtener la lista de profesores
        })

def get_profesores():
    with connection.cursor() as cursor:
        query = "SELECT DISTINCT nombre FROM programacion_academica ORDER BY nombre"
        cursor.execute(query)
        rows = cursor.fetchall()
    return [row[0] for row in rows]


"""
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.db import connection
from django.utils.safestring import mark_safe
import plotly.io as pio

@login_required_custom
def prorrateo(request):
    user_avatar = request.session.get('user_avatar', '')
    user_name = request.session.get('user_name', '')
    user_lastname = request.session.get('user_lastname', '')
    user_roles = request.session.get('user_roles', [])
    user_email = request.session.get('user_email', '')

    if request.method == 'POST':
        profesor_seleccionado = request.POST.get('profesor')

        # Ejecutar consulta SQL
        with connection.cursor() as cursor:
            query = """
                SELECT ins.nombre AS nombre_x, pa.nombre AS nombre_y, ins.prog_acad AS programa
                FROM inscripciones ins
                JOIN programacion_academica pa ON pa.n_clase = ins.n_clase
                WHERE pa.nombre = %s
            """
            cursor.execute(query, [profesor_seleccionado])
            rows = cursor.fetchall()

        # Convertir los resultados a un DataFrame de pandas
        df = pd.DataFrame(rows, columns=['nombre_x', 'nombre_y', 'programa'])

        # Agrupar los datos por profesor y programa y contar los estudiantes únicos
        df_grouped = df.groupby(['nombre_y', 'programa'])['nombre_x'].nunique().reset_index()
        df_grouped = df_grouped.rename(columns={'nombre_x': 'num_estudiantes'})

        # Calcular el número total de estudiantes por profesor
        total_students_per_professor = df_grouped.groupby('nombre_y')['num_estudiantes'].sum()

        # Calcular el porcentaje de estudiantes por programa para cada profesor
        df_grouped['percentage'] = df_grouped.apply(lambda row: row['num_estudiantes'] / total_students_per_professor[row['nombre_y']] * 100, axis=1)

        # Extraer los datos para el profesor deseado
        data_profesor = df_grouped[df_grouped['nombre_y'] == profesor_seleccionado]

        # Crear la gráfica de pie
        fig_pie = px.pie(data_profesor, values='percentage', names='programa', title=f'{profesor_seleccionado} - Distribución por Programa',
                         hover_data=['num_estudiantes'], labels={'num_estudiantes':'Número de estudiantes'})

        # Crear la gráfica de barras
        fig_bar = px.bar(data_profesor, x='programa', y='percentage', title=f'{profesor_seleccionado} - Porcentaje por Programa',
                         labels={'percentage':'Porcentaje de Estudiantes (%)'}, text='percentage')

        # Convertir los gráficos a HTML
        pie_graph_html = pio.to_html(fig_pie, full_html=False)
        bar_graph_html = pio.to_html(fig_bar, full_html=False)

        return render(request, 'prorrateo.html', {
            'user_avatar': user_avatar,
            'user_name': user_name,
            'user_lastname': user_lastname,
            'user_roles': user_roles,
            'graph_html_pie': mark_safe(pie_graph_html),
            'graph_html_bar': mark_safe(bar_graph_html),
            'profesores': get_profesores()  # Asegúrate de definir esta función para obtener la lista de profesores
        })

    else:
        # Para GET, simplemente mostrar la página con el formulario
        return render(request, 'prorrateo.html', {
            'user_avatar': user_avatar,
            'user_name': user_name,
            'user_lastname': user_lastname,
            'user_roles': user_roles,
            'graph_html_pie': '',  # No mostrar gráfico al principio
            'graph_html_bar': '',  # No mostrar gráfico al principio
            'profesores': get_profesores()  # Asegúrate de definir esta función para obtener la lista de profesores
        })

def get_profesores():
    with connection.cursor() as cursor:
        query = "SELECT DISTINCT nombre FROM programacion_academica ORDER BY nombre"
        cursor.execute(query)
        rows = cursor.fetchall()
    return [row[0] for row in rows]

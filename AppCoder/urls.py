from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('courses', views.courses, name='courses'),
    path('profesores', views.profesores, name='profesores'),
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('entregables', views.entregables, name='entregables'),
    path('search_commission', views.search_commission, name="search_commission"),
    path('search', views.search),
    # Paths apartir de la clase 22 (playground avanzado):
    path('leer_profesores', views.leer_profesores, name = 'leer_profesores'),
    path('eliminar_profesor/<profesor_nombre>/', views.eliminar_profesor, name = "eliminar_profesor"),
    path('editar_profesor/<profesor_nombre>/', views.editar_profesor, name = "editar_profesor"),

    # Urls: de clases basadas en vistas:
    path('curso/list', views.CursoList.as_view(), name = 'List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name = 'Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name = 'New'),
    path(r'^editar(?P<pk>\d+)$', views.CursoUpdate.as_view(), name = 'Edit'),
    path(r'borrar^(?P<pk>\d+)$', views.CursoDelete.as_view(), name = 'Delete'),
]
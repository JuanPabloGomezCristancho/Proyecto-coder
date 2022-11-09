from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor
from AppCoder.forms import Course_form, Profesor_form

# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def courses(request):
    if request.method == 'POST':
        form = Course_form(request.POST) # Llega toda la informacion del Html.
        print(form)
        if form.is_valid: # Lo valida Django
            information = form.cleaned_data
            curso = Curso( nombre=information['nombre'], comision=information['comision'])
            curso.save()
            return render(request, "AppCoder/courses.html", {"form": Course_form()})
    
    return render(request, "AppCoder/courses.html", {"form": Course_form()})


def search_commission(request):
    return render(request, "AppCoder/search_commission.html")

def search(request):
    if request.GET["commission"]:
        commission = request.GET["commission"]
        courses = Curso.objects.filter(comision__icontains=commission)

        return render(request, "AppCoder/search_results.html", {"courses": courses, "commission":commission})
    
    else:
        answer = "No se enviaron datos"
    
    return HttpResponse(answer)


# Vistas hechas en la clase 22:

def leer_profesores(request):
    profesores = Profesor.objects.all()
    contexto = {"profesores":profesores}
    return render(request, "AppCoder/leer_profesores.html", contexto)

def profesores(request):

    if request.method == 'POST':
        form = Profesor_form(request.POST) # Llega toda la informacion del html.
        print(form)
        if form.is_valid: # Lo valida Django
            information = form.cleaned_data
            profesor = Profesor( nombre=information['nombre'], apellido=information['apellido'], email=information['email'], profesion=information['profesion'])
            profesor.save()
            return render(request, "AppCoder/inicio.html")
    
    return render(request, "AppCoder/profesores.html", {"form": Profesor_form()})


def eliminar_profesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre = profesor_nombre)
    profesor.delete()

    profesores = Profesor.objects.all()
    contexto = {"profesores":profesores}

    return render(request, "Appcoder/leer_profesores.html", contexto)

def editar_profesor(request, profesor_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    profesor = Profesor.objects.get(nombre=profesor_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        form = Profesor_form(request.POST)
        print(form)
        if form.is_valid:  # Si pasó la validación de Django

            informacion = form.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/leer_profesores.html", {"profesores":Profesor.objects.all()})
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        form = Profesor_form(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editar_profesor.html", {"form": form})





# Clases basadas en vistas:
# Importaciones:

from django.views.generic import ListView
class CursoList(ListView):
    model = Curso
    template_name = 'Appcoder/cursos_list.html'

from django.views.generic.detail import DetailView
class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

from django.views.generic.edit import CreateView

class CursoCreacion(CreateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'comision']

from django.views.generic.edit import UpdateView
class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'comision']

from django.views.generic.edit import DeleteView
class CursoDelete(DeleteView):
    model = Curso
    success_url = "/AppCoder/curso/list"


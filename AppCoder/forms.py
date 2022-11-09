from django import forms

class Course_form(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()

# Forms a partir de la clase 22:

class Profesor_form(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
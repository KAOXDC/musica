from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.

def canciones_view (request):
    lista = Musica.objects.filter()
    return render(request, 'artista/canciones.html', locals())

''' seccion de autenticacion '''

def login_view (request):
    return render(request, 'artista/login.html', locals())

def logout_view (request):
    return render(request, 'artista/logout.html', locals())

def register_view (request):
    return render(request, 'artista/register.html', locals())

''' Seccion del artista '''

def agregar_musica_view (request):
    #esta vista agrea una cacion  por cada artista 
    usuario = User.objects.get(id = request.user.id) # usuario que esta conectado en el momento 
    

    if request.method == 'POST':
        formulario = agregar_musica_form(request.POST, request.FILES)
        if formulario.is_valid():
            m = formulario.save(commit= False)
            m.artista = usuario
            m.save()
            return redirect('/mi_musica/')
    else:
        formulario = agregar_musica_form()
    return render(request, 'artista/musica_agregar.html', locals())

def mi_musica_view (request):
    usuario = User.objects.get(id = request.user.id)
    lista = Musica.objects.filter(artista = usuario)
    return render(request, 'artista/mi_musica.html', locals())

def editar_musica_view (request):
    return render(request, 'artista/editar_musica.html', locals())

def ver_musica_view (request,id_musica):
    object = Musica.objects.get(id = id_musica)
    return render(request, 'artista/musica_ver.html', locals())



def eliminar_musica_view (request):
    return render(request, 'artista/eliminar_musica.html', locals())

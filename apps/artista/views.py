from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import *
# Create your views here.

def canciones_view (request):
    lista = Musica.objects.filter()
    return render(request, 'artista/canciones.html', locals())

''' seccion de autenticacion '''

def login_view (request):
    usu = ""
    cla = ""
    if request.method == 'POST':
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario = authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/')
            else: 
                msj = 'usuario o clave incorrectos'
    
    formulario = login_form()
    return render(request, 'artista/login.html', locals())

def logout_view (request):
    logout(request)
    return redirect ('/login/')

def register_view (request):

    formulario = register_form()
    if request.method == 'POST':
        formulario = register_form(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            correo = formulario.cleaned_data['email']
            password_1 = formulario.cleaned_data['password_1']
            password_2 = formulario.cleaned_data['password_2']
            u = User.objects.create_user(username= usuario, email= correo, password= password_2, is_superuser=True, is_staff=True)
            u.save()
            return redirect('/login/')
        else:
            return render(request, 'artista/register.html', locals())        
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

    # canciones = Musica.objects.all() # retorna una lista con todas las canciones

    #artista = User.objects.get(username = 'admin') # obtiene un objeto artista
    #canciones = Musica.objects.filter(artista = artista) # obtiene una lista de canciones por el artista 
    
    # obtiene una lista de canciones por el artista 'admin' y el nombre de la cancion es 'musica 1
    # canciones = Musica.objects.filter(artista__username = 'admin' , nombre = 'musica 1' ) 
    
    # retornar una lista de canciones que contengan en el nombre la palabra 'ica'  
    #canciones = Musica.objects.filter(nombre__icontains = 'ICA' ) 
    
    # retornar una lista de canciones que contengan en el nombre la palabra 'ica' y que el username contenga 'ADMIN'
    # canciones = Musica.objects.filter(nombre__icontains = 'ICA', artista__username__icontains = 'ADMIN', artista__is_active__icontains=1) 

    #canciones = Musica.objects.filter(nombre__startswith = 'e') # buscar una cancion que inice por 'e'
    #canciones = Musica.objects.filter(nombre__endswith = 'e') # buscar una cancion que finalice por 'e'

    # print ("xxxxxxxxxxxxxxxx")
    # print (canciones)
    # print ("xxxxxxxxxxxxxxxx")
    return render(request, 'artista/mi_musica.html', locals())

def editar_musica_view (request):
    return render(request, 'artista/editar_musica.html', locals())

def ver_musica_view (request,id_musica):
    object = Musica.objects.get(id = id_musica)
    return render(request, 'artista/musica_ver.html', locals())



def eliminar_musica_view (request):
    return render(request, 'artista/eliminar_musica.html', locals())

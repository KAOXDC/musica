from django.urls import path
from .views import *

urlpatterns = [
    # pagina de inicio de todas las canciones
    path('', canciones_view, name='canciones'),
    
    # urls de autenticacion
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    
    # urls del artista
    path('agregar_musica/', agregar_musica_view, name='agregar_musica'),
    path('mi_musica/', mi_musica_view, name='mi_musica'),
    path('ver_musica/<int:id_musica>/', ver_musica_view, name='ver_musica'),
    path('editar_musica/<int:id_musica>/', editar_musica_view, name='editar_musica'),
    path('eliminar_musica/<int:id_musica>/', eliminar_musica_view, name='eliminar_musica'),

    path('dos_forms/',dos_forms_view, name='dos_forms'),


    path('ejemplo/',ejemplo_view, name='ejemplo'),
]
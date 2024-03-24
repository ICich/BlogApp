from django.urls import path, include
from BlogApp.views import * #Importo todas las vistas

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    #User
    path("login/", login_request, name="login"),
    path("register/", registro, name="register"),
    path("logout/", cerrar_sesion, name="logout"),
    path("usredit/", editar_perfil, name="editarUsuario"),
    path("addavatar/", agregar_avatar, name="agregarAvatar"),
    #Post
    path("create/", post_create, name="post_create"),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('posts/', post_list, name='post_list'),
    path('post/<int:pk>/update/', post_update, name='post_update'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
]
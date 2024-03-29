from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from BlogApp.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from BlogApp.forms import *
from django.contrib.auth.decorators import login_required #usar @login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


# Create your views here.

def index(request):
    posts = Post.objects.order_by('-published_date')[:3]
    return render(request, 'BlogApp/index.html', {"is_index_page": True,"posts": posts})

def about(request):
    return render(request, "BlogApp/about.html")

#USUARIOS

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirige a la página de inicio
                return redirect('index')
        else:
            return render(request, "BlogApp/index.html", {"mensaje": "Datos incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, "BlogApp/usr_login.html", {"form": form})



def registro(request):
    if request.method == "POST":
        
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "BlogApp/index.html", {"mensaje":f"Usuario creado"})
            
    else:
        
        form = UserRegistrationForm()
        
    return render (request, "BlogApp/usr_register.html", {"form": form})


@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            informacion = form.cleaned_data
            
            usuario.email = informacion.get("email")
            usuario.last_name = informacion.get("last_name")
            usuario.first_name = informacion.get("first_name")


            usuario.save()

            return redirect('index')

    else:
        
        form = UserEditForm(initial={"first_name": usuario.first_name,
                                       "last_name": usuario.last_name,
                                        "email": usuario.email,})


    return render(request, "BlogApp/usr_edit.html", {"form": form})  



def agregar_avatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            actualUser = request.user
            try:
                # Verificar si el usuario ya tiene un avatar
                avatar = Avatar.objects.get(user=actualUser)
                # Si ya tiene un avatar, actualizarlo con la nueva imagen
                avatar.image = form.cleaned_data["image"]
            except Avatar.DoesNotExist:
                # Si el usuario no tiene un avatar, crear uno nuevo
                avatar = Avatar(user=actualUser, image=form.cleaned_data["image"])
            avatar.save()
            return redirect("index")
    else:
        form = AvatarFormulario()
    return render(request, "BlogApp/add_avatar.html", {"form": form})          
        
            
def cerrar_sesion(request):
    logout(request)
    return redirect("index")


#CRUD

#Create
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'BlogApp/post_create.html', {'form': form})

#Read
#Listar todos
def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'BlogApp/post_list.html', {'posts': posts})

#Detalles de un post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'BlogApp/post_detail.html', {'post': post})

#Update
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Verificar si el usuario actual es el propietario del post o es un administrador
    if request.user == post.owner or request.user.is_staff:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'El post se ha actualizado correctamente.')
                return redirect('post_detail', pk=pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'BlogApp/post_update.html', {'form': form})
    else:
        # Si el usuario no tiene permiso para editar el post, redirigir a otra página o mostrar un mensaje de error
        return render(request, 'permission_denied.html')
    
#Delete
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.owner or request.user.is_staff:
        if request.method == 'POST':
            post.delete()
            return redirect('post_list')  # Redirige a la lista de posts después de borrar
        return render(request, 'BlogApp/post_delete.html', {'post': post})
    else:
        return render(request, 'permission_denied.html')
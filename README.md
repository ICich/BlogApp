# BlogApp  

El proyecto en desarrollo, consta de un Blog con tematica de ciclismo, realizado con el framework Django.

## Autor
Desarrollado por Ignacio Cichero.

## Requerimientos
* Python: Este puede ser descargado desde [python.org](https://www.python.org/downloads/)
* Django: Este puede ser instalado con el comando `pip install django`

## Uso
1. Primero realizar las migraciones si es necesario, con el comando: `python manage.py makemigrations`
2. Seguido, aplica las migraciones con el comando: `python manage.py migrate`
3. Navega hasta la carpeta del proyecto que contiene el archivo "manage.py".
4. Ejecuta el servidor Django usando el comando `python manage.py runserver`.
5. Accede a la aplicación en tu navegador web visitando `http://localhost:8000`.

## URLS
Los urls funcionales son:

* Página de inicio: http://localhost:8000/BlogApp/
* Acerca de: http://localhost:8000/BlogApp/about/
* Iniciar sesión: http://localhost:8000/BlogApp/login/
* Registro de usuario: http://localhost:8000/BlogApp/register/
* Cerrar sesión: http://localhost:8000/BlogApp/logout/
* Editar perfil de usuario: http://localhost:8000/BlogApp/usredit/
* Agregar avatar: http://localhost:8000/BlogApp/addavatar/
* Crear un nuevo post: http://localhost:8000/BlogApp/create/
* Detalle de un post específico: http://localhost:8000/BlogApp/post/<id_del_post>/
* Lista de todos los posts: http://localhost:8000/BlogApp/posts/
* Actualizar un post existente: http://localhost:8000/BlogApp/post/<id_del_post>/update/
* Eliminar un post existente: http://localhost:8000/BlogApp/post/<id_del_post>/delete/

## Video demostracion
[Link video](https://drive.google.com/file/d/1S9Mh91CncXAJMZ6-AeLn3lbwpvWKVPHu/view?usp=drive_link)

# BlogApp  

El proyecto en desarrollo, consta de un Blog con tematica de ciclismo, realizado con el framework Django.

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

**/AppMantenimiento/nuevo_mecanico/: URL para agregar un nuevo mecánico.  
**/AppMantenimiento/nuevo_vehiculo/: URL para agregar un nuevo vehículo.  
**/AppMantenimiento/nuevo_mantenimiento/: URL para agregar un nuevo mantenimiento.  
**/AppMantenimiento/buscar_mecanico/: URL para buscar un mecánico.  

# BlogApp  

El proyecto en desarrollo, consta de un Blog con tematica de ciclismo, realizado con el framework Django.

## Requerimientos
* Python: Este puede ser descargado desde [python.org](https://www.python.org/downloads/)
* Django: Este puede ser instalado con el comando `pip install django`

## Orden
1. Primero hacer las migraciones si es necesario: `python manage.py makemigrations`
2. Seguido el migrate: `python manage.py migrate`
3. Finalmente para correr el servidor: `python manage.py runserver`

## URLS
Los urls funcionales son:

**/AppMantenimiento/nuevo_mecanico/: URL para agregar un nuevo mecánico.  
**/AppMantenimiento/nuevo_vehiculo/: URL para agregar un nuevo vehículo.  
**/AppMantenimiento/nuevo_mantenimiento/: URL para agregar un nuevo mantenimiento.  
**/AppMantenimiento/buscar_mecanico/: URL para buscar un mecánico.  

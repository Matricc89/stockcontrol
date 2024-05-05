# Stock Control

App que permite agregar Proveedores y Productos, listarlos con sus detalles.
Editar y eliminarlos.

## Autor

Matias Ricci

## Instrucciones

1. Crear y activar entorno virtual

- Windows

python -m venv venv

.\venv\Scripts\activate

- Linux 

python3 -m venv venv

source venv/bin/activate

2. Instalar las dependencias

pip install -r requirements.txt

3. Navegar hacia la carpeta del proyecto

cd src

4. Crear las migraciones que son una "plantilla" para crear la base de datos con la que trabajará nuestro proyecto de Django

python manage.py makemigrations

5. Ejecutar la migración para crear la base de datos con la que trabajará nuestro proyecto de Django

python manage.py migrate

6. Crear el superusuario para nuestro proyecto de Django, solo si no se ha creado

python manage.py createsuperuser

Ingrese Username, Email address y Password.

7. Levantar el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto http://127.0.0.1:8000/

python manage.py runserver

Es hora de ir al navegador y en una pestaña nueva navegar hacia "http://127.0.0.1:8000"
# Pixel Arcade

Sitio Django para administrar y consultar el catálogo de productos, categorías, proveedores, novedades y eventos de Pixel Arcade.

## Tecnologías

- Python 3.11 o superior
- Django 5.2
- MySQL
- PyMySQL
- python-decouple

## Configuración local

1. Crea y activa un entorno virtual.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Copia `.env.example` a `.env` y configura una clave secreta y credenciales válidas de MySQL.
4. Crea la base de datos indicada en `DB_NAME` y concede acceso al usuario indicado en `DB_USER`.
5. Ejecuta `python manage.py makemigrations` y `python manage.py migrate`.
6. Crea un usuario administrador con `python manage.py createsuperuser`.
7. Inicia el servidor con `python manage.py runserver` y abre `http://127.0.0.1:8000/`.

El catálogo y las novedades se administran desde Django Admin. `.env` y la base de datos local no se incluyen en Git.
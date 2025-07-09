Proyecto Final del curso de Python dictado en Coder House

Proyecto Final - OSORIO (Blog) El proyeto final se trata de un blog personal en el cual debe poseer el formato clásico de ese tipo de sitio web (con detalles de la página como el título, la fecha de publicación, la página, texto, imágenes, etc). Además, de la navegación del blog y la posibilidad de "postear" nuevas publicaciones, posee un login y un signup para la creación del usuario. El cual, podrá mantener actualizdos los datos y estando en estado de "logueado" podrá editar y borrar publicaciones.

ProyectoFinal_OSORIO2/ └── mi_blog/ ├── manage.py ├── mi_blog/ # configuración del proyecto ├── blog/ # aplicación principal

📦 Requisitos Python 3.10 o superior Django 5.x (ver también archivo requirements.txt)

Se trata de una aplicación web construida con Django y escrita en Python. Por lo que, para poder acceder al mismo y poder visualizarlo y usarlo correctamente. Deberán seguir los siguientes pasos: Crear el entorno virtual (opcional pero recomendado) Ingresa a VisualCode - Nueva Terminal - y en la misma escribe lo siguiente: python -m venv env (si estas en Mac )es python3 -m venv env

Clonar el repositorio

Ingresa a VisualCode - Nueva Terminal - y en la misma escribe lo siguiente:

git clone https://github.com/mato83/ProyectoFinal_OSORIO2.git

Una vez finalizada la clonación, muévete en la terminal a la carpeta del proyecto, ingresando lo siguiente: cd ProyectoFinal_OSORIO2/mi_blog

3_ Instalar dependencias

El archivo requirements.txt ya está en el proyecto, por lo tanto, no es necesario que lo instales. Sin embargo, sería bueno asegurarse que tienes la paquetería PIP actualizada.

En la terminal ingresa lo siguiente: pip install --upgrade pip

4_Aplicar migraciones Ingresar en la terminal en el proyecto raíz (mi_blog), lo siguiente: python manage.py migrate (si es para MAC: python3 manage.py migrate o python3 manage.py makemigrations) y luego pip install django (como ya está incluído el archivo requirements.txt, no hace falta instalarlo pero en todo caso, para poder hacerlo debes escribir pip install -r requirements.txt )

5_Creación de un superusuario Para esto primero debemos ir "Nueva terminal" y luego entrar al Shell a través del siguiente código: python manage.py shell (python3 manage.py shell)

Dentro del Shell de Django ingresar lo siguiente: from django.contrib.auth import get_user_model; User=get_user_model(); User.objects.create_superuser('admin','admin@example.com','contraseña_segura')

Tener en cuenta, que también, puedes crear un usuario desde el Shell ingresando lo siguiente: from django.contrib.auth.models import User User.objects.create_superuser('admin', 'admin@example.com', 'tu_contraseña_segura')

6_ Ejecutar el servidor python manage.py runserver

e ingresar al servidor local: http://127.0.0.1:8000/

Notas adicionales Compatible con Windows, macOS y Linux

Contacto matiasosorio83@gmail.com
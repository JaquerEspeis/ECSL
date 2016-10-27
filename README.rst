Sitio genérico público para ECSL
###########################################

Una propuesta para la elaboración de un sitio libre y reutilizable para la Comunidad Centroamericana.

Instalación
################

Este sitio está basado en Django 1.10.

Clone este repositorio

.. code::bash

    git clone https://github.com/JaquerEspeis/ECSL.git
    cd ECSL
    
Cree un entorno virtual

.. code::bash

   mkdir ~/entornos
   virtualenv -p python3 ~/entornos/ecsl
   source ~/entornos/ecsl/bin/activate
   pip install --upgrade pip setuptools
   
Instale las dependencias del sistema

.. code::bash

   pip install -r requirements.txt
   
Cree la base de datos

.. code::bash

   python manage.py migrate
   python manage.py createsuperuser
   
Corra la aplicación 

.. code::bash

  python manage.py runserver

en otra terminal ejecute un cliente de corre

.. code::bash

  python -m smtpd -n -c DebuggingServer localhost:1025

  

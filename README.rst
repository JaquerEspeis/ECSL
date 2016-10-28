Sitio genérico público para ECSL
###########################################

Una propuesta para la elaboración de un sitio libre y reutilizable para la Comunidad Centroamericana.

Está desarrollado en respuesta a los requerimientos del sitio_.

.. _sitio: http://ecsl2017.softwarelibre.ca/index.php/Comisi%C3%B3n_de_Sistemas_y_Dise%C3%B1o_Gr%C3%A1fico

Instalación
################

Este sitio está basado en Django 1.10.

Clone este repositorio

.. code:: bash

    git clone https://github.com/JaquerEspeis/ECSL.git
    cd ECSL
    
Cree un entorno virtual (puede necesitar virtualenv instalado en la máquina **$ apt-get install python-virtualenv** )

.. code:: bash

    mkdir ~/entornos
    virtualenv -p python3 ~/entornos/ecsl
    source ~/entornos/ecsl/bin/activate
    pip install --upgrade pip setuptools
   
Instale las dependencias del sistema

.. code::bash

    pip install -r requirements.txt
   
Cree la base de datos

.. code:: bash

    python manage.py migrate
    python manage.py createsuperuser
   
Corra la aplicación 

.. code:: bash

    python manage.py runserver

en otra terminal ejecute un cliente de correo

.. code:: bash

    python -m smtpd -n -c DebuggingServer localhost:1025


Contribuciones 
##################

Puede contribuir con este proyecto haciendo pull request al repositorio.

Busque en la wiki un requerimiento no satisfecho hasta ahora, cree una nueva app y agreguela.

Si el requerimiento tiene relación con alguna app ya existente puede agregarlo al app 

El sitio está pensado para ser multilenguaje, vea dentro del código como soportarlo.



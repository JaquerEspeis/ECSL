Sitio genérico público para ECSL
###########################################

Una propuesta para la elaboración de un sitio libre y reutilizable para la Comunidad Centroamericana.

Instalación
################

Este sitio está basado en Django 1.10.

Clone este repositorio

    git clone https://github.com/JaquerEspeis/ECSL.git
    cd ECSL
    
Cree un entorno virtual

   mkdir ~/entornos
   virtualenv -p python3 ~/entornos/ecsl
   source ~/entornos/ecsl/bin/activate
   pip install --upgrade pip setuptools
   
Instale las dependencias del sistema

   pip install -r requirements.txt
   
Cree la base de datos

   python manage.py migrate
   python manage.py createsuperuser
   
Corra la aplicación 

  python manage.py runserver

en otra terminal ejecute un cliente de corre

  python -m smtpd -n -c DebuggingServer localhost:1025

  

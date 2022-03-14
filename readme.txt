configuration du projet
creation environnement virtuel: 
         python -m venv env
Activier l'environnement:
        env\Scripts\activate.bat
installer les depedance:
        pip install django
        pip install djangorestframework
creer le projet:
        django-admin startproject projet       
------------------------------------------------------------------------------------------------------------------------
telecharger les dependance à l'aide de cette commande 
     Activier l'environnement
        env\Scripts\activate.bat

     pip install -r requirements.txt

     pip freeze > requirements.txt : permet d'ajouter les dependance dans requirements.txt
----------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------
Demarrer l'application en allant dans le dossier project_gestion_memoire grace à la ligne de commande avec:

     cd project_gestion_memoire
     python manage.py runserver

------------------------------------------------------------------------------------------------------------------------
les lien utils
    la documentation de l'api grace à ce lien  https://drf-yasg.readthedocs.io/en/stable/readme.html
------------------------------------------------------------------------------------------------------------------------

python manage.py createsuperuser --username admin --email admin@gmail.com

------------------------------------------------------------------------------------------------------------------------
lancer 

docker-compose up
------------------------------------------------------------------------------------------------------------------------
postgres
 connect:  psql -U postgres
 create db: createdb -U postgres gestion_immo

heroku
 heroku config:set SECRET_KEY=sfgfdghdgdhgdghghdsghdghsdghghdhgdhgddh
 heroku config:set EMAIL_USER=sarrabdoulaye93@gmail.com
 heroku config:set EMAIL_PASSWORD=python.classesmates.pass 
 pip install django-heroku
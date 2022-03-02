'''
TRILHA DE APRENDIZADO

Introduction And Installation
Url Routing And Django Apps
Django Template Language
Sending Data To Template File
Building A Word Counter In Django
Get vs Post In Django
Static Files In Django
Introduction To Django Models
Django Admin Panel & Manipulation of Database
User Registration In Django
User Login And Logout In Django
Dynamic Url Routing In Django
Postgresql Setup
'''


#  INTRODUCTION AND INSTALLATION

'''
__________________
YOUTUBE TUTORIAL

Have python installed in your computer

    $ python
    
    python version 3.10.1
    Django version 4.0

Python was install with pip module

    $ pip install --upgrade pip    

Install Django on your system computer
https://docs.djangoproject.com/en/4.0/topics/install/#installing-official-release

    $ pip install django




__________________
PYTHON VIRTUAL ENVIRONMENT

Python virtual machine environment, a self-contained directory tree 
that contains a Python installation for a particular version of Python,
plus a number of additional packages.
https://docs.python.org/3/tutorial/venv.html

Install a virtual Environment 
    
    $ pip install virtualenvwrapper-win
    
Create a virtual environment in Django project
     
    $ mkvirtualenv myapp    
    
Enter in project directory, init the virtual machine, and so install the Django

    (myapp) C:\xx\xx> $ pip install django
    
Activate the environment
navigate at "C:\Users\italo\OneDrive - Fundação Mineira de Educação e Cultura\Python\Free Code Camp - Python Backend Web Development Course (with Django)\Django Crash Course"
    
    $ workon myapp
    $ tutorial-env\Script\activate.bat
    
Deactivate the environment 
    
    $ deactivate
    
Django version

    $ python -m django --version




__________________    
CREATE A NEW DJANGO PROJECT

Django has this command line, which allows you to create a new project
Enter at directory you want create a project with terminal
    
    $ django-admin startproject myproject

Django project files
https://docs.djangoproject.com/en/4.0/intro/tutorial01/#creating-a-project

Run the server

    $ python manage.py runserver
__________________
CREATE A SUB DJANGO PROJECT

Init the virtual environment (myapp)

    $ python manage.py startapp myapp
    



__________________   
DJANGO TUTORIAL

Create a virtual environment in Django project
         
    $ python -m venv tutorial-env    
'''




# URL ROUTING AND DJANGO APPS ----- rever 3:59:49

'''
ARQUIVO myproject\'urls.py
- Adicionar o <include> nos imports do 'django.urls'.
- Adicionar uma 'path' as 'urlpatterns', incluindo o arquivo de url do outro projeto 

ARQUIVO myapp\'urls.py
- importar o modulo 'path' do Django
- importar a página 'views' 
- criar a 'urlpatterns'
-  
'''




# DJANGO TEMPLATE LANGUAGE

'''
Create a new folder 'templates'
myproject\'settings.py 
Into templates -> DIRS
    ''DIRS': [BASE_DIR, 'templates'],'
No arquivo 'views.py', retorne:
    return render(request, 'first_page.html')

'''




# SENDIND DATA TO TEMPLATE FILE

'''
Adicione um parametro no retorno do view
    Por convenção, retornamos o 'context'
    
Dentro de templates/first_page.html,
adicione no texto HTML a sintaxe para
acessar os dados
    {{name}}
    {{age}}
'''




# BUILDING A WORD COUNTER IN DJANGO

'''
Adcione o atributo 'method=""' na tag form
Adicione o atributo 'name="words"' na tag textarea
    o 'name' será o nome do atributo passado pelo método do forms
Ao clicar no 'input type="submit"', você verá que o texto
    esta sendo enviado pela url
Adicione o atributo 'action=""' na tag form 
'''




# GET VS POST IN DJANGO

'''
CSRF token

'''




# STATIC FILES IN DJANGO

'''
Static files is any external file that we use in your template file

First, Create a static folder, where located all the static files.

Tell to Djando where is located all the static files:
Enter in 'settings.py' file:
    import os # windows    
Bellow the 'STATIC_URL' command, enter:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )    
    # BASE_DIR -> mean the root directory of this project
    
Todas vez que for importar um arquivo, utilize a seguinte sintaxe

    <link rel="stylesheet" href="{% static 'style.css' %}">
    # {% static 'name file' %}
    
Adicione no inicio do arquivo que você queira importar
    {% load static %}

ADD A TEMPLATE FROM BOOTSTRAPMADE IN YOUR PROJECT

Baixe o arquivo de template e cole no diretório raiz do projeto, exemplo;
    myproject\Arsha

Caso já tenha criado alguma página index.html dentro do diretório
templates, pode apaga-lá

Transfira o arquivo index.html que tenha vindo do template bootstrap
para dentro da pasta templates do seu projeto

Transfira a pasta 'assets' que veio no template bootstrap para a 
pasta 'static' do seu projeto

Abra o arquivo 'index.html' e insira a formatação necessário do Django
para importar arquivos estáticos 
No topo do arquivo 'index.html' insira:
        {% load static %}
Em cada referência a arquivos staticos, insira a sintaxe:     "{% static '' %}"
    old:
        <img src="assets/img/clients/client-6.png" class="img-fluid" alt="">
    new:
        <img src="{% static 'assets/img/clients/client-6.png' %}" class="img-fluid" alt="">
'''




# MODELS

'''
A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re storing.
Generally, each model maps to a single database table.

No arquivo models.py:

- create a new model:

    class Feature:
        id: int
        name: str
        details: str

No arquivo views.py:

- import the models:

    from .models import Feature

- Na função index,
instancie uma model,
preencha os seus atributos,
e passe o model como parametro.

    def index(request):
        feature1 = Feature()
        feature1.id = 0
        feature1.name = 'Fast'
        feature1.details = 'Our service is very quick'
        return render(request, 'index.html', {'feature': feature1})
    
No arquivo index.html:

- Subistitua os pontos onde 
deseja inserir os dados do model.
Exemplo:

    <h4><a href="">{{feature.name}}</a></h4>
    
Agora você ja pode instanciar vários models
e passa-lós como parametro, para depois
iteramos sobre os vários models.

Para iterar sobre vários models:

    {% for feature in features %}
    
    {% endfor %}
'''




# Django Admin Panel & Manipulation Of Database

'''
Change class model to attend the models creation.
Exemplo:

    class Feature(models.Model):
        name = models.CharField
        
Acesse o arquivo 'settings.py':
Em 'INSTALLED_APPS', insira o nome da aplicação, ex:
    '',
    'myapp'
    
INTEGRATING DATABASES
Acesse o diretório da aplicação pelo terminal,
execute o comando:

    $ pythom manage.py makemigrations
    
Save changes and send all these changes
into our database. 

    $ python manage.py migrate
    
Agora acesse o Django Admin

    http://localhost:8000/admin
    
Volte para prompt de comando para podermos
criar um usuário administrador para o painel admin.

    $ python manage.py createsuperuser

Informe um nome,
informe um email (opcional),
informe uma senha e
repita a mesma senha.

Agora volte ao painel e insira os dados 
do usuário recém criado.

No painel do admin, clique um 'Users'
to see all the users I have in my project.

CREATE DATABASE NAME FEATURE
AND
MIGRATE THAT INTO OUR DATABASE

from .models import Feature

# Register your models here.
admin.site.register(Feature)

Agora no Django Admin, será possível
criar novos 'Features' in 'MYAPP'

Apague todos os Features criado no arquivo 'views.py',
e crie novamento todos pelo painel admin.

DATA THAT I HAVE IN MY VIEWS
Tenha certeza de importa o models Feature no arquivo 'views.py',
pois com este arquivo poderemos acessar os dados do database.

Para fazermos isso, continuando no arquivo 'views.py',
crie a variavél

    features = Feature.objects.all()
'''



















![TELA_1.jpg](MEUIMOVEL_WB/blob/main/MEUIMOVEL_WEB/static/img/TELA_1.jpg)


### DIRETRIZES PARA CRIAÇÃO DO SITE MEUIMOVEL

 1) INSTALAR GIT NO COMPUTADOR ( CONTROLE DE VERSÃO)
 2) ENTRAR NO PYCHARM E INICIAR NOVO PROJETO CONSIDERANDO O AMBIENTE VIRTUAL VENV
 3) CRIAR UM ARQUIVO README.MD
 4) INICIAR INSTALAÇÃO DO FRAMEWORK DJANGO PARA DESENVOLVIMENTO WEB DO MEUIMOVEL 
  

# DIFERENÇAS ENTRE FUNCIONALIDADES DO DJANGO E DESCRIÇÃO DA ESTRUTURA DO SITE MEUIMOVEL. 
Consideramos  o MEUIMOVEL_PROJECT/MEUIMOVEL_WEB como um diretório pai onde será realizado a organização de todos os arquivos.
O subdiretorio MEUIMOVEL_WEB/MEUIMOVEL_WEB é o projeto django criado a partir do comando django-admin startproject MEUIMOVEL_WEB,
em que consideramos como pacote do python que abrange todas as configurações da instancia do django e do banco de dados.
Podemos criar o aplicativo central do site a partir do código "python manage.py startapp core", que incorpora as 
funcões utilizadas no site, "marcar como realizado" e criar nova tarefa - dentro do arquivo "views.py".
 
# A ESTUTURA FINAL DO PROGRAMA FICARÁ
```
    MEUIMOVEL_WEB
    │
    ├───core                        # Core App
    │   │   admin.py
    │   │   apps.py
    │   │   models.py
    │   │   tests.py
    │   │   views.py
    │   │   __init__.py
    │   ├───migrations
    ├───static                     
    │   ├───css
    │   └───fonts
    │   └───img
    │   └───js
    ├───templates                     # Templates para render dos dados data
    │       base.html
    └───MEUIMOVEL_WEB                   # aplicativo padrao criado pelo django
        │   asgi.py
        │   settings.py
        │   urls.py
        │   wsgi.py
        │   __init__.py
        └───__pycache__

 
 
## INICIAR GIT PARA CONTROLE DE VERSÃO (terminal windows)
```
git init
git >> README.md
git add README.md
git commit -m "Meu primeiro Commit para criação do Portal MEU IMÓVEL "
git branch -M main
git remote remove origin
git remote add origin https://github.com/Gustavomendss/MEUIMOVEL_WB.git
git push -u origin main
-  Para verificar as mudanças usar o  "git status"
```
### Instalando o FrameWork Django
pip install django

# RESUMO DO FRAMEWORK DJANGO
    __init__.py é um arquivo em branco que instrui o Python a tratar esse diretório como um pacote Python.
    settings.py contém todas as definições do website. É onde nós registramos qualquer aplicação que criarmos, a localização de nossos arquivos estáticos, configurações de banco de dados etc.
    urls.py define os mapeamentos de URL para visualização do site. Mesmo que esse arquivo possa conter todo o código para mapeamento de URL, é mais comum delegar apenas o mapeamento para aplicativos específicos, como será visto mais adiante.
    wsgi.py é usado para ajudar na comunicação entre seu aplicativo Django e o web server. Você pode tratar isso como um boilerplate.
    O script manage.py é usado para criar aplicações, trabalhar com bancos de dados, e iniciar o webserver de desenvolvimento.



### Iniciando o projeto DJANGO (terminal console)
```
django-admin startproject MEUIMOVEL_WEB
cd MEUIMOVEL_WEB                   #INDO ATÉ A PASTA RAIZ (terminal console)
```
### Iniciando um aplicativo DJANGO (terminal console)
``` 
python manage.py startapp core
```
## CRIANDO UM ARQUIVO PARA GRAVAR AS ALTERACOES
    1. ABRIR TERMINAL E DIGITAR :
```
    python manage.py makemigrations       # Cria os arquivos de migração 
    python manage.py migrate              # Cria as tabelas no db
```


# A ESTUTURA FICARÁ ASSIM 
```
    ├───core                        # Core App
    │   │   admin.py
    │   │   apps.py
    │   │   models.py
    │   │   tests.py
    │   │   views.py
    │   │   __init__.py
    │   └───migrations 
    ├───templates                     # Templates para render dos dados data
    │    └───base.html
    └─── MEUIMOVEL_WEB                   # aplicativo padrao criado pelo django
        │   asgi.py
        │   settings.py
        │   urls.py
        │   wsgi.py
        │   __init__.py
        └───__pycache__
```

## CONFIGURACAO DO SETTINGS.PY

    1. IR ATE O CAMINHO ~\MEUIMOVEL_PROJECT\MEUIMOVEL_WEB\MEUIMOVEL_WEB\SETTINGS.PY
    2. IMPORTAR "os" e MODIFICAR O  'INSTALLED_APPS E ADICIONAR  O TEXTO 'core'
    3. PARA CORRETO DIRECIONAMENTO DOS TEMPLATES E ARQUIVOS CONSIDERAR CODIGO
```
      'DIRS': [os.path.join(BASE_DIR, 'templates')],
```
    3. ALTERAR SECCAO  LANGUADE_CODE PARA 'pt-br' e TIME_ZONE PARA 'AMERICA/Sao_paulo'
    4. ADICIONAR O CAMINHO PARA ARQUIVOS ESTÁTICOS A SEREM UTILIZADOS NO CSS
```
         STATIC_URL = '/static/'
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, "static"),
            #'/var/www/static/',
        ]
        STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn') # CDN REFERE SE A CONTENT DELIVERY NETWORK
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')
        # QUE É A MESMA COISA QUE C:\Users\GUSTAVO\PycharmProjects\MEUIMOVEL_PROJECT\MEUIMOVEL_WEB\media_cnd
```
    5. FECHAR ARQUIVO SETTINGS.PY
      - PARA VERIFICAR O BASE DIR DIGITAR NO CONSOLE "RUNSERVER"

## CONFIGURACAO DO MODELS.PY (core)
    1. IR ATE O CAMINHO ~\MEUIMOVEL_PROJECT\MEUIMOVEL_WEB\core\models.py
    2. CRIANDO CLASSES ABSTRATAS:
``` 
       from django.db import models
        import os
        # CRIANDO O  MODELO PARA O MEUIMOVEL

        class Base(models.Model):
            criacao = models.DateTimeField(auto_created=True)
            atualizacao = models.DateTimeField(auto_now=True)
            ativo = models.BooleanField(default=True)

            class Meta:
                abstract = True

        class MEUIMOVELapp(Base):
            título = models.CharField(max_length=255)
            url = models.URLField(unique=True)


            class Meta:
                verbose_name = 'MEUIMOVEL'
                verbose_name_plural = 'MEUIMOVEL'


            def __str__(self):
                return self.título

        # Criando a parte de avaliacao
        class Avaliacao(Base):
            MEUIMOVEL = models.ForeignKey(MEUIMOVELapp,
                                       related_name='avaliacoes',
                                       on_delete=models.CASCADE)
            nome = models.CharField(max_length=255)
            email = models.EmailField()
            comentario = models.TextField(blank=True, default='')
            avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

            class Meta:
                verbose_name = 'Avaliação'
                verbose_name_plural = 'Avaliações'
                unique_together = ['email','MEUIMOVEL']

                def __str__(self):
                    return f'{self.nome} avaliou o MEUIMOVEL {self.MEUIMOVEL} com a nota {self.avaliacao}'

        class todo(models.Model):
            name = models.TextField(max_length=255)
            status = models.BooleanField(default=False)
```

## CRIANDO UM SUPERUSUÁRIO PARA ADICIONAR O MODELO NA PAGINA DE ADMINISTRAÇÃO
python manage.py createsuperuser

- usuario : admin
- email   : admin@admin.com
- senha   : admin

    1. IR ATE O CAMINHO ~\MEUIMOVEL_PROJECT\MEUIMOVEL_WEB\core\admin.py
    2. : Digitar:
 ```   
    from .models import MEUIMOVELapp, Avaliacao
    from django.contrib import admin
    from .models import todo
    
    @admin.register(MEUIMOVELapp)
    class MEUIMOVELAdmin(admin.ModelAdmin):
        list_display = ('título','url', 'criacao', 'atualizacao','ativo')
    
    @admin.register(Avaliacao)
    class AvaliacaoAdmin(admin.ModelAdmin):
        list_display = ('MEUIMOVEL','nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')
    
    admin.site.register(todo)
```

##  GRAVAR AS ALTERACOES 
    1. ABRIR TERMINAL E DIGITAR :
    python manage.py makemigrations       # Cria os arquivos de migração 
    python manage.py migrate              # Cria as tabelas no db



## Alterando a view do site para navegação do url
    A ideia é que o usuário seja capaz de ver as tarefas a serem realizas,
    adicionar novas tarefas e eliminar as tarefas já concluídas .
    Para essas três operações, temos três visualizações diferentes em nosso aplicativo MEUIMOVEL. 
    - O primeiro é o índice, que renderiza todas as tarefas desfeitas. (index)
    - A Segunda visão é a new_to_do, que  permite ao usuário adicionar um novo à lista
    - A terceira visão é a mark_as_done que permite o usuário concluír a tarefa. 
    
    A ideia de ter um campo booleano no modelo para todo é simples. 
    Suponha a criação de um campo booleano e considere uma tarefa como "concluída",
    se o status da tarefa for igual a  verdadeiro (1). E por padrão, o status da tarefa é falso (0). 
    Portanto, para as visualizações do índice e new_to_do, podemos filtrar os objetos com base no status e,
    em seguida renderizar no modelo. 
    Assim, o usuário  terá apenas a lista de tarefas pendentes que não foram realizadas. 
    
    Chegando à visão mark_as_done, enviamos o id da tarefa que é feita a partir do template/base.html e então
    recuperamos o objeto e tornamos o campo de status da tarefa True.


## ALTERANDO A VIEW
    1. IR ATE O CAMINHO ~\MEUIMOVEL_PROJECT\MEUIMOVEL_WEB\core\views.py
    2. CRIANDO CLASSES ABSTRATAS:
   ```     
        
        from django.shortcuts import render
        from django.http import HttpResponse
        
        from .models import todo
        
        def home_view(request,*args, **kwargs):
            return HttpResponse("<h1>Hello World</h1>")
        
        def index(request):
            list_todo = todo.objects.filter(status=False)
            return render(request, 'base.html', {'list_todo': list_todo})
        
        
        def mark_as_done(request, id):
            obj = todo.objects.get(pk=id)
            obj.status = True
            obj.save()
            list_todo = todo.objects.filter(status=False)
            return render(request, 'base.html', {'list_todo': list_todo})
        
        def new_todo(request):
            if request.method == "POST":
                todo.objects.create(name=request.POST.get('todo-name'))
                list_todo = todo.objects.filter(status=False)
                return render(request, 'base.html', {'list_todo': list_todo})
        
```

# Criar os arquivos da pasta static (css/fonts/img/js) - lista na fonte abaixo


## CRIANDO A VISÃO DO TEMPLATE EM HTML (base.html)
```
{% load static %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">

  <title>

        {% block title %}
            MEUIMOVEL Application
        {% endblock %}


    </title>
    <link rel="shortcut icon" href="/static/img/favicon.png"/>
    <!link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="/static/css/font-awesome.min.css">
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
    <!link rel="stylesheet" href='/static/css/base.css'/>
  </head>

  <body>
    <div class="container">
      <div class="container">
        <p>
        </p>
      </div>
    </div>
    <p>

    {% load static %} <img src="/static/img/home.png" alt="home" style="width:1024px;height:340px />

    </p>


    <div class="col-sm-7">
        <div class="row">
          <div class="col-sm-12">
            <div class="panel panel-default text-left">
              <div class="panel-body">
                <h4 contenteditable="true">Olá bem-vindo ao MEUIMOVEL ! <br>
                    Liste aqui todas as suas tarefas e matenha a organização. &#9200; &#128079
                    </h4>
              </div>
            </div>
          </div>
        </div>

            <h2>
          Lista de Tarefas
        </h2>

        <div class="row">
          <div class="col-sm-9">
          {% for todo in list_todo %}
            {% if not todo.status %}
                <div class="well">
                  <h4>{{ todo.name }}</h4>
                  <a href="{% url 'mark_as_done' todo.id  %}">Marcar como realizado   &#9989;</a>
                </div>
            {% endif %}
          {% endfor %}
          </div>
        </div>

        <h2>
          Criar nova tarefa
        </h2>
      </div>

        <div class="col-sm-9">
          <div class="well">
            <form method="POST" action="{% url 'new_todo' %}" id="input-text" method="post" enctype="multipart/form-data">
              {% csrf_token %}
              <input type="textarea" style="width: 450px;" name="todo-name">
              <button type="submit" value="Submit" class="btn btn-primary">Criar uma nova tarefa </button>
            </form>
          </div>
        </div>


    <div class="row">
      <button onclick="myFunction()">Realizar Logout!</button>
    </div>


  </div>
  </div>
</div>
</body>

<style>

body {
  background-color: #EEEEEE;
  color: black;
}
.dark-mode {
  background-color: black;
  color: black;
}

.parent {
  position: relative;
  top: 0;
  left: 0;
}

.text-center {
  text-align: center;
}

h2 {
margin: 20px 20px

}



</style>

<script>
  function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-mode");
  }
</script>
</html>
```

# O ARQUIVO HTML POSSUI ALGUNS DETALHES IMPORTANTES
    Temos dois lugares importantes nas linhas 35–50, em que  a lista de tarefas desfeitas é exibida 
    e cada tarefa tem um id, que é usado para tornar a tarefa lida.
    Na linha 44, enviamos o id da tarefa enviado junto com a url e na visualização a tarefa é marcada como lida. 
    E nas linhas 51 a 64 temos outro local importante, onde uma solicitação de postagem é feita e enviada. 
    A linha 58-62 cobre este aspecto do envio de dados usando os formulários e a solicitação é tratada pela
    visão de new_todo. Esqueci de mencionar que um botão para o modo escuro também foi habilitado e, ao clicar
    no botão, cada elemento que for branco ficará escuro e vice-versa.


## Alterando a url do site para redirecionamento correto da midia e links 
    1. IR ATE O CAMINHO ~\MEUIMOVEL_PROJECT\MEUIMOVEL_WEB\MEUIMOVEL_WEB\urls.py
    2. DIGITAR :
```
      from django.contrib import admin
      from django.urls import include, path
      from core import views
      from django.conf import settings
      from django.conf.urls.static import static
      from django.contrib.staticfiles.urls import staticfiles_urlpatterns
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('', views.index, name='index'),
          path('new-todo', views.new_todo, name="new_todo"),
          path('mark-as-done/<int:id>', views.mark_as_done, name="mark_as_done"),
      
      ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
      
      urlpatterns += staticfiles_urlpatterns()
```
#PARA CRIAR O DIRETORIO DE ARQUIVOS LOCAIS PARA PRODUCAO ( IRA CRAR PASTA static_cdn)
```
python manage.py collectstatic
```

## RODANDO O APLICATIVO 
```
python manage.py runserver
```
# PARA SAIR APERTAR CTRL+C NO TERMINAL


# upload no git
```
git add .
git commit -m " MEUIMOVEL  - Finalizado !"
git push -u origin main
```

## Fontes
https://pythonacademy.com.br/blog/o-comando-makemigrations-do-django
https://python.plainenglish.io/how-to-make-a-simple-to-do-app-in-python-django-ead5b35b9d98
https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/skeleton_website
https://www.mytecbits.com/internet/python/addding-image-django-web-app
https://tutorial.djangogirls.org/pt/django_start_project/
https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css
https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css
https://img.icons8.com/nolan/64/tasklist.png
https://www.youtube.com/watch?v=YH-ipgxlJzs
https://cssgradient.io/

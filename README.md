# Python-Mod8DjangoBasico
Curso do Luiz Otávio Miranda de Django.
Projeto Django Básico super básico. Um simples hello world em HTML e em HTTPResponse.

# PARTE 1 - OLÁ MUNDO

## Instalação
No terminal, digitar: 
```bash
pip install django
```

Opcional, para versões específicas, substituir o x e digitar:
```bash
pip install django==x.x.x
```

## Conceitos Básicos

- Apps
    - São as páginas. Exemplo: site.com/index. site.com/about. site.com/carrinho. São 3 diferentes apps de um mesmo site. É similar as 'activities' dos aplicativos Android.
- !TODO

## Iniciando, base pra tudo

### Criando o projeto

Pra criar o primeiro projeto, é preciso, ao invés de criar pastas, usar comandos no terminal. A criação da pasta mãe é essencial.

```bash
django-admin startproject projeto .
```
* O ponto . se refere a pasta atual que o terminal está localizado. Então essa pasta mestra será criada nesse local.
> Nota: O **projeto** pode ter qualquer nome. Desde que não seja abstrato por convenção. Aqui é usado um exemplo abstrato 'projeto'.

![image](https://user-images.githubusercontent.com/98990221/194149374-385b0277-e4d0-4970-b4de-07bbcc0ccaef.png)

### Arquivos gerados dentro da pasta 'projeto'

- **init.py** diz para o interpretador que ali não é uma pasta qualquer, e sim um pacote.
- **settings.py** é importantíssimo. Irei colocar todos os apps instalados em INSTALLED APPS.
- **urls.py** é outro importante. Assim como settings, esse arquivo referencia os apps e linka isso com formato url.
- **wsgi.py** (web server gateway interface) é relacionado ao servidor web. Faz o trabalho de hospedar em um server para o site ser visualizado por todos. O projeto por hora será local, portanto isso nem será mexido.

### Arquivo gerado fora da pasta 'projeto'
- **manage.py** é extremamente importante e não deve ser tocado por hora.

## Iniciando um servidor super básico

Pra preparar um servidor bem básico de testes, usamos também o terminal, com o auxílio do **manage.py** mencionado anteriormente.

```bash
python3 manage.py runserver
```
* Por padrão, ele irá rodar na porta 8000
```bash
python3 manage.py runserver 8888
``` 
* Muda a porta.

> Nota: Aparecerá um suposto erro de migration. Tem a ver com base de dados, e isso será corrigido depois, não há motivos para preocupação agora.

## Criando o primeiro app (página) básico

Criar um app requer também o uso do terminal.

```bash
python3 manage.py startapp blog
```

> Nota: 'blog' pode ser qualquer coisa.

Será criada uma pasta chamada *blog* na raíz do projeto (nesse caso, em Mod8DjangoBasico). Esse é o nosso primeiro "app".

![image](https://user-images.githubusercontent.com/98990221/194149765-37dabfc0-2104-4c33-b586-968a4cd52afd.png)

### Arquivos Úteis
- **apps.py** - configuração do app. Usamos o nome 'BlogConfig', que é o nome da Classe, lá na settings.py em 'projeto'.
- **views.py** - TODO

### Arquivos Inúteis POR HORA:
- **Pasta migrations** está relacionada a base de dados. Não será abordado nesse rep.
- **admin.py** registra a área administrativa do site 'blog'. Não há preocupação por hora sobre isso.
- **models.py** trabalha com a base de dados, e está diretamente relacionado com migrations. Não será abordado nesse rep.
- **tests.py** envolve testes automatizados.

## Sync após a criação de um app - settings.py

Criar um app também requer que mudanças sejam feitas em outros arquivos de forma a registrar essa nova criação. No caso será registrado em DOIS locais importantes: **settings.py** e **urls.py**, ambos na pasta 'projeto' desse rep.

* Em *projeto/settings.py*, acrescentar no array **INSTALLED APPS**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',  # Obrigatório registrar os apps criados aqui
]
```
* Exemplo abstrato: 
```python
'fulano.apps.FulanoConfig'  # FulanoConfig é uma classe gerada automaticamente localizada em blog/apps.py
```

## Sync após a criação de um app - urls.py

Agora a parte mais chata envolve modificar a urls.py na pasta mãe. Primeiro é preciso criar uma **urls.py** vazia na pasta 'blog'.

![image](https://user-images.githubusercontent.com/98990221/194153121-67eccde7-6b7b-446a-a423-d43cdca01432.png)

### urls.py na pasta blog

Deixar dessa forma:

```python
from django.urls import path
from . import views  # Importa o arquivo views.py da própria pasta (.) que o urls.py se encontra.

# Crio uma list urlpatterns = [] igual a do arquivo na pasta mãe.
urlpatterns = [
    path('', views.index)  # Não executo o método com (), só referencio
    # Está em '' pois referencia ao próprio url site.com/blog/.
]
```
* Exemplo abstrato:
```python
path('posts/', view.index)  # Cria uma url nova site.com/blog/posts/.
```

### urls.py na pasta mãe (projeto)

Deixar dessa forma:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Isso será acrescentado
]
```

* Exemplo abstrato: 
```python
path('sicrano/', include('sicrano.urls'))
```

> Nota: Isso referencia o **urls.py** da **pasta blog**.

## Primeiro Olá mundo!

Esse **index** em **urls.py** faz referência ao método index() NÃO EXECUTADO (pois não tem parênteses) no arquivo **views.py**. O arquivo views.py está vazio. No caso é pra por o método 'def index(request): pass' por hora nele

Em **views.py**, excrever:

```python
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):  # Nome do método poderia ser qualquer um. Index é convenção. O nome request também é convenção. Toda vida é feito um request ao abrir a página.
    return HttpResponse("Olá mundo!")
```

* Esse método **HttpResponse** é um print básico em web.


Ao abrir o site e atualizar, ir na seção /blog/ do site irá aparecer 'Olá mundo!'.

## Para trabalhar com HTML:

Criar uma pasta **templates** dentro do app desejado. Dentro da pasta **templates**, criar uma pasta com o mesmo nome da pasta do app. No caso 'blog'.

```raíz/blog/templates/blog```

Dentro da pasta */blog/templates/blog/*, criar um html simples chamado **index.html**.

No mesmo arquivo views.py do app, trocamos o HttpResponse por:

```python
from django.shortcuts import render  # Esse método 'render' é o que projeta o arquivo HTML em nossa página

def index(request):
    return render(request, 'blog/index.html')
```

* No arquivo **index.html**, escrever **Olá Mundo!** em linguagem html. Atualizar a página. Agora temos Olá mundo em html nativo.

# PARTE 2 - HERANÇA DE HTML

Normalmente o site tem sub-páginas html que herdam características da página principal. Ao invés de criar vários index.html pra várias páginas (apps) em html no Copia-Cola, vamos usar um arquivo **base.html** que serve de herança para outros index.html em **subpáginas**.

##
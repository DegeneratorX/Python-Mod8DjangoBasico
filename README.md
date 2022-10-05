# Python-Mod8DjangoBasico
Curso do Luiz Otávio Miranda de Django.
Projeto Django Básico super básico. Um simples hello world em HTML e em HTTPResponse.

## Instalação
No terminal, digitar: 
    ```pip install django```

Opcional, digitar:
```pip install django==x.x.x```
- Substituir o x pela versão específica que se deseja instalar.

## Conceitos Básicos

- Apps
    - São as páginas. Exemplo: site.com/index. site.com/about. site.com/carrinho. São 3 diferentes apps de um mesmo site. É similar as 'activities' dos aplicativos Android.
- !TODO

## Iniciando, base pra tudo

Pra criar o primeiro projeto, é preciso, ao invés de criar pastas, usar comandos no terminal. A criação da pasta mãe é essencial.

- ```django-admin startproject projeto .```
    - O ponto . se refere a pasta atual que o terminal está localizado. Então essa pasta mestra será criada nesse local.
    - O 'projeto' pode ter qualquer nome. Desde que não seja abstrato por convenção. Aqui é usado um exemplo abstrato 'projeto'.
- init.py diz para o interpretador que ali não é uma pasta qualquer, e sim um pacote.
- settings.py é importantíssimo. Irei colocar todos os apps instalados em INSTALLED APPS.
- urls.py é outro importante. Assim como settings, esse arquivo referencia os apps e linka isso com formato url.
- wsgi.py (web server gateway interface) é relacionado ao servidor web. Faz o trabalho de hospedar em um server para o site ser visualizado por todos. O projeto por hora será local, portanto isso nem será mexido.

Fora da pasta 'projeto', é criado um arquivo chamado 'manage.py'. Esse arquivo também é extremamente importante e não deve ser tocado por hora.

# Iniciando um servidor super básico

Pra preparar um servidor bem básico de testes, usamos também o terminal, com o auxílio do manage.py mencionado anteriormente.

- python3 manage.py runserver
    - Por padrão, ele irá rodar na porta 8000
    - 'python3 manage.py runserver 8888' muda a porta.
- Aparecerá um suposto erro de migration. Tem a ver com base de dados, e isso será corrigido depois, não há motivos para preocupação agora.

# Criando o primeiro app (página) básico

Criar um app requer também o uso do terminal.

- python3 manage.py startapp blog
- Será criada uma pasta chamada 'blog' na raíz do projeto (nesse caso, em Mod8DjangoBasico). Esse é o nosso primeiro app.
- Arquivos úteis:
    - apps.py - configuração do app. Usamos o nome 'BlogConfig', que é o nome da Classe, lá na settings.py em 'projeto'.
    - views.py - TODO
- Arquivos inúteis POR HORA:
    - Pasta migrations está relacionada a base de dados. Não será abordado nesse rep.
    - admin.py registra a área administrativa do site 'blog'. Não há preocupação por hora sobre isso.
    - models.py trabalha com a base de dados, e está diretamente relacionado com migrations. Não será abordado nesse rep.
    - tests.py envolve testes automatizados.

# Sync após a criação de um app - settings.py

Criar um app também requer que mudanças sejam feitas em outros arquivos de forma a registrar essa nova criação. No caso será registrado em DOIS locais importantes: settings.py e urls.py, ambos na pasta 'projeto' desse rep.

- Em settings.py, acrescentar no array 'INSTALLED APPS'
    - 'blog.apps.BlogConfig'
    - Exemplo abstrato: 'fulano.apps.FulanoConfig'

# Sync após a criação de um app - urls.py

Agora a parte mais chata envolve modificar a urls.py na pasta mãe. Primeiro é preciso criar uma urls.py vazia na pasta 'blog'. Deixar vazia por hora.

- No urls.py da pasta mãe (projeto), importar o 'include' de django.urls.
- Acrescentar na list 'urlpatterns'
    - path('blog/', include('blog.urls'))
    - Exemplo abstrato: path('sicrano/', include('sicrano.urls'))
    - 

Isso referencia o urls.py da pasta 'blog'. Mas lá ainda não tem nada. Agora vamos preencher esse arquivo.

- No urls.py da pasta blog:
    - from django.urls import path
    - from . import views
        - Importa o arquivo views.py da própria pasta (.) que o urls.py se encontra.
- Criar uma list urlpatterns = [] igual a do arquivo na pasta mãe.
- Acrescentar na list 'urlpatterns'
    - path('', views.index)
        - Referencia ao próprio /blog/
    - path('posts/', view.index)
        - Referencia /blog/posts

# Primeiro Olá mundo!

- Esse 'index' em urls.py faz referência ao método index() NÃO EXECUTADO (pois não tem parênteses) no arquivo views.py. O arquivo views.py está vazio. No caso é pra por o método 'def index(request): pass' por hora nele

- Além disso, no mesmo arquivo, escrever:
    - from django.http import HttpResponse
        - Esse método 'HttpResponse' é um print básico em web.
        - Dentro do método index(), escrever 'return HttpResponse('Olá mundo!')

Ao abrir o site e atualizar, ir na seção /blog/ do site irá aparecer 'Olá mundo!'.

# Para trabalhar com HTML:

- Criar uma pasta 'templates' dentro do app desejado. Dentro da pasta 'templates', criar uma pasta com o mesmo nome da pasta do app. No caso 'blog'.

- Dentro da pasta /blog/templates/blog/, criar um html simples chamado 'index.html.

- No mesmo arquivo views.py:
    - from django.shortcuts import render
        - Esse método 'render' é o que projeta o arquivo HTML em nossa página
        - Dentro do método index(), escrever 'return render(request, 'blog/index.html')

- No arquivo 'index.html', escrever 'Olá Mundo!' em linguagem html. Atualizar a página. Agora temos Olá mundo em html nativo.
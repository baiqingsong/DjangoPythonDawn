# Django的基本使用

* [简介](#简介)
* [Django安装](#django安装)
* [创建项目](#创建项目)
* [创建应用](#创建应用)
* [URL配置](#url配置)
* [Templates](#templates)
* [Models](#Models)
* [Admin](#admin)
* [其他](#其他)

## 简介
Django是一个基于python的高级web框架，它能够让开发者高效并且快速的开发。高度集成，并且开源  
[https://www.djangoproject.com/](https://www.djangoproject.com/)  

## Django安装
启用命令行pip指令安装Django框架
```
pip install Django==1.11.7
```

## 创建项目
打开命令行输入
```
django-admin startproject myblog
```
创建名称为myblog的项目  
项目目录  
manage.py   与项目交互的命令行工具集的入口  
可以通过manage.py命令启动自带的Django服务器  
```
python manage.py runserver
```
最后可以跟端口号，不加默认8000  

wsgi.py     WSGI(Python Web Server Gateway Interface)  
Python服务器网关接口，Python应用与web服务器之间的接口，不建议修改  

urls.py        URL配置文件  
Django项目中的所有地址（url）都需要我们自己去配置其URL  

settings.py    项目的总配置文件  
包含了数据库，web应用，时间等配置  
BASE_DIR       项目根目录  
SECRET_KEY     项目的安全码  
DEBUG          debug调试  
ALLOWED_HOSTS   允许访问的地址，如果有值，则只允许值的地址进行访问，其他将会屏蔽  
INSTALLED_APPS   Django创建的应用，如果我们创建应用需要写进去  
ROOT_URLCONF    指向的是URL配置文件  
DATABASES      数据库配置，默认sqlite3，如果需要更改访问
[https://docs.djangoproject.com/en/1.11/ref/settings/#databases](#https://docs.djangoproject.com/en/1.11/ref/settings/#databases)  
STATIC_URL     静态文件的地址  

## 创建应用
需要利用到manage.py命令，再命令行中输入
```
python manage.py startapp blog
```
创建名称为blog的应用  
注：要将应用名添加到settings.py中的INSTALLED_APPS里  
应用目录  
migrations        数据移植（迁移）模块，内容自动生成  
admin.py          该应用的后台管理系统配置  
apps.py           该应用的一些配置，Django1.9以后自动生成  
models.py         数据模块，使用ORM框架  
tests.py          自动化测试模块，Django提供了自动化测试功能，再这个编写测试化脚本（语句）  
views.py          执行相应的代码所在模块，代码逻辑处理的主要地点  
项目中大部分代码写再views.py中  

## URL配置
一般项目中会有很多应用，为了看起来简洁，所以最好在每个应用中都添加一个urls.py  
然后在项目名对应的urls.py中添加include其他应用下的urls.py  

## Templates
HTML文件，使用了Django模板语言（Django Template Language， DTL），可以使用第三方模块（如Jinja2）  
创建一个Template  
1. 在app的根目录下创建名叫Templates的目录  
2. 在该目录下创建一个HTML文件  
3. 在views.py中返回render()  
render需要三个参数，第一个request，第二个html文件，第三个是后台传给前端的数据  
DTL的初步使用  
render()函数中支持一个dict类型的参数  
该字典是后台传递到模板的参数，键为参数名，在模板中使用{{参数名}}来直接使用  
注：Django按照INSTALLED_APPS中的添加顺序查找Templates 
不同APP下Templates目录中的同名.html文件会造成冲突  
解决：在APP的Templates目录下创建一个同名APP名称的目录  
将html文件放到新创建的目录下  

## Models
通常，一个Model对应数据库中的一张数据表  
Django中Models以类的形式表现  
它包含了一些基本字段以及数据的一些行为  
ORM  
对象关系映射（Object Relation Mapping）  
实现了对象和数据库之间的映射  
隐藏了数据的访问细节，不需要编写SQL语句  
编写Models步骤：
1. 在应用根目录下创建models.py，并引用models模块，创建应用时自动实现  
2. 创建类，继承models.Model，该类既是一张数据表  
3. 在类中创建字段  
字段创建：  
字段即类里面的属性（变量），例如：  
attr = models.CharField(max_length=64)  
创建model后生成数据表，需要用到manage.py命令
```
python manage.py makemigrations app名（可选）
python manage.py migrate
```
Django会自动在app/migrations/目录下生成移植文件  
执行python manage.py sqlmigrate 应用名 文件id 查看SQL语句  
默认sqlite3的数据库在项目的根目录下db.sqlite3  
查看并编辑db.sqlite3，使用第三方软件（SQLite Expert Personal）  
查看数据库中的信息:  
views.py中import models  
article = models.Article.objects.get(pk=1)
render(request, page, {'article' : article})

## Admin
Admin时Django自带的一个功能强大的自动化数据管理界面  
被授权的用户可以直接在Admin中管理数据库  
Django提供了许多针对Admin的定制功能  
配置Admin：  
1. 创建一个超级用户（python manage.py cteatesuperuser）  
2. Admin入口（localhost:8000/admin/）  
3. 修改settings.py中的LANGUAGE_CODE='zh-Hans',将后台变成中文  
4. 在应用下admin.py中引用自身的models模块（或里面的模型类）  
5. 编辑admin.py : admin.site.register(models.Article),Article是要注册的类  
6. 在Article中添加一个方法  
7. 根据Python版本选择(python3)__str__(self)或(python2.7)__unicode__(self)  

## 其他
html中的for循环：  
{% for xx in xxs %}  
{% endfor %}  
href后面的地址：  
{% 'app_name:url_name' param %}  
设置命名空间： 
根urls.py中添加
```
    url(r'^blog/', include('blog.urls', namespace='blog')),
```
应用的urls.py中添加
```
    url(r'^article_page/(?P<article_id>[0-9]+)', views.article_page, name='article_page'),
```
响应函数：  
使用request.POST['参数名']获取表单数据  
POST提交表单，必须在前端页面中添加
```
{% csrf_token %}
```
过滤器  
写在模板中，属于Django语言  
可以改变模板中的变量，从而显示不同的内容  
形式{{ value | filter }}  
例如： {{ list_nums | length }}  
Django Shell  
它是一个Python的交互命令行程序  
自动引入了我们的项目环境  
我们可以使用它与我们的项目进行交互  
使用命令行
```
python manage.py shell
```
Admin中显示更多字段  
1. 创建admin配置类  
class ArticleAdmin(admin.ModelAdmin)  
注册：admin.site.register(Article, ArticleAdmin)  
2. 显示其他字段  
list_display = ('title', 'content')
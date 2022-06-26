# Django

---

## Linux 上安装 Django

- https://www.djangoproject.com/download/

```bash
pip3 install Django
```

**验证**
```bash
python3
import django
django.VERSION
```

---

## Django 管理工具

**django-admin**

```
✦ ❯ django-admin

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
```

---

## 创建项目

```bash
django-admin startproject testweb
```

创建完成后可以查看下项目的目录结构
```bash
cd testweb
tree
├── manage.py
└── testweb
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

# manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
# testweb: 项目的容器。
# testweb/asgi.py: 一个 ASGI 兼容的 Web 服务器的入口，以便运行你的项目。
# testweb/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
# testweb/settings.py: Django 项目的设置/配置。
# testweb/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
# testweb/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。
```

启动服务器
```bash
python3 manage.py runserver 0.0.0.0:5000
```

**常见问题**

- Django 遇到 Invalid HTTP_HOST header
    - 修改 settings.py ALLOWED_HOSTS 值为 `'*'`
        ```py
        ALLOWED_HOSTS = ['*']
        ```

**视图和 URL 配置**

testweb 目录新建一个 views.py 文件
```py
from django.http import HttpResponse

def hello(request):
    return HttpResponse("test1")
```

修改 urls.py
```py
from . import views

urlpatterns = [
    path('hello/', views.hello),
]
```

**path() 函数**

Django path() 可以接收四个参数，分别是两个必选参数：route、view 和两个可选参数：kwargs、name。

语法格式：
```
path(route, view, kwargs=None, name=None)

route: 字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 view。
view: 用于执行与正则表达式匹配的 URL 请求。
kwargs: 视图使用的字典类型的参数。
name: 用来反向获取 URL。
```

---

## debug

settings.py
```py
DEBUG = False
```

---

## Source & Reference

- https://www.runoob.com/django/django-template.html
- https://www.runoob.com/django/django-model.html
- https://www.runoob.com/django/django-views.html

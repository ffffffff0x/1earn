# flask

https://dormousehole.readthedocs.io/en/latest/quickstart.html

---

## 安装

```bash
pip3 install Flask
```

---

## 使用

一个最小的 Flask 应用如下
```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

首先我们导入了 Flask 类。该类的实例将会成为我们的 WSGI 应用。

接着我们创建一个该类的实例。第一个参数是应用模块或者包的名称。 `__name__` 是一个适用于大多数情况的快捷方式。有了这个参数， Flask 才能知道在哪里可以找到模板和静态文件等东西。

然后我们使用 `route()` 装饰器来告诉 Flask 触发函数 的 URL 。

函数返回需要在用户浏览器中显示的信息。默认的内容类型是 HTML ，因此字 符串中的 HTML 会被浏览器渲染。

把它保存为 hello.py 或其他类似名称。请不要使用 flask.py 作为应用名称，这会与 Flask 本身发生冲突。

可以使用 flask 命令或者 python 的 -m 开关来运行这个应 用。在运行应用之前，需要在终端里导出 FLASK_APP 环境变量：

```bash
export FLASK_APP=hello
flask run
flask run --host=0.0.0.0
```

如果文件名为 app.py 或者 wsgi.py ，那么不需要设置 FLASK_APP 环境变量。

**常见问题**

- 老版本的 Flask

    版本低于 0.11 的 Flask ，启动应用的方式是不同的。简单的说就是 flask 和 python -m flask 命令都无法使用。在这种情 况下有两个选择：一是升级 Flask 到更新的版本，二是学习其他启动服务器的方法。

- 非法导入名称

    FLASK_APP 环境变量中储存的是模块的名称，运行 flask run 命令就 会导入这个模块。如果模块的名称不对，那么就会出现导入错误。出现错误的时机是在 应用开始的时候。如果调试模式打开的情况下，会在运行到应用开始的时候出现导入 错误。出错信息会告诉您尝试导入哪个模块时出错，为什么会出错。

    最常见的错误是因为拼写错误而没有真正创建一个 app 对象。

### 开发功能

flask run 命令不只可以启动开发服务器。如果您打开调试模式，那么服务 器会在修改应用代码之后自动重启，并且当请求过程中发生错误时还会在浏览器 中提供一个交互调试器。

调试器允许执行来自浏览器的任意 Python 代码。虽然它由一个 pin 保护， 但仍然存在巨大安全风险。不要在生产环境中运行开发服务器或调试器。

```bash
export FLASK_ENV=development
flask run
```

### 路由

```py
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

### 变量规则

通过把 URL 的一部分标记为 `<variable_name>` 就可以在 URL 中添加变量。标记的 部分会作为关键字参数传递给函数。通过使用 `<converter:variable_name>` ，可以 选择性的加上一个转换器，为变量指定规则。请看下面的例子:
```py
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

### 唯一的 URL / 重定向行为

以下两条规则的不同之处在于是否使用尾部的斜杠。
```py
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

projects 的 URL 是中规中矩的，尾部有一个斜杠，看起来就如同一个文件 夹。访问一个没有斜杠结尾的 URL （ /projects ）时 Flask 会自动进行重 定向，帮您在尾部加上一个斜杠（ /projects/ ）。

about 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这 个 URL 时添加了尾部斜杠（`/about/` ）就会得到一个 404 “未找到” 错 误。这样可以保持 URL 唯一，并有助于搜索引擎重复索引同一页面。

### URL 构建

url_for() 函数用于构建指定函数的 URL。它把函数名称作为第一个 参数。它可以接受任意个关键字参数，每个关键字参数对应 URL 中的变量。未知变量 将添加到 URL 中作为查询参数。

```py
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

```
/
/login
/login?next=/
/user/John%20Doe
```

### HTTP 方法

Web 应用使用不同的 HTTP 方法处理 URL 。当您使用 Flask 时，应当熟悉 HTTP 方法。 缺省情况下，一个路由只回应 GET 请求。 可以使用 route() 装饰器的 methods 参数来处理不同的 HTTP 方法:
```py
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

如果当前使用了 GET 方法， Flask 会自动添加 HEAD 方法支持，并且同时还会 按照 HTTP RFC 来处理 HEAD 请求。同样， OPTIONS 也会自动实现。

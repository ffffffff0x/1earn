# SSTI

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**相关文章**
- [一篇文章带你理解漏洞之 SSTI 漏洞](https://www.k0rz3n.com/2018/11/12/%E4%B8%80%E7%AF%87%E6%96%87%E7%AB%A0%E5%B8%A6%E4%BD%A0%E7%90%86%E8%A7%A3%E6%BC%8F%E6%B4%9E%E4%B9%8BSSTI%E6%BC%8F%E6%B4%9E/)
- [利用SSTI漏洞获取服务器Shell](https://xz.aliyun.com/t/2637)

**相关工具**
- [epinna/tplmap](https://github.com/epinna/tplmap) - ssti 检测工具
- https://github.com/VikasVarshney/ssti-payload - SSTI Payload Generator
- [payloadbox/ssti-payloads](https://github.com/payloadbox/ssti-payloads) - Server Side Template Injection Payloads

**靶场**
- [s4n7h0/xvwa](https://github.com/s4n7h0/xvwa) - 存在 SSTI 的环境

---

# 基础

**什么是模板**

模板引擎可以让（网站）程序实现界面与数据分离，业务代码与逻辑代码的分离，这大大提升了开发效率，良好的设计也使得代码重用变得更加容易。

模板引擎也扩展了黑客的攻击面。除了常规的 XSS 外，注入到模板中的代码还有可能引发 RCE（远程代码执行）。通常来说，这类问题会在博客，CMS，wiki 中产生。虽然模板引擎会提供沙箱机制，攻击者依然有许多手段绕过它。

**什么是 SSTI**

1. 如果攻击者能够控制要呈现的模板，服务端接收了用户的恶意输入以后，未经任何处理就将其作为 Web 应用模板内容的一部分，模板引擎在进行目标编译渲染的过程中，执行了用户插入的可以破坏模板的语句，就可能导致上下文数据的暴露，甚至在服务器上运行任意命令的表达式。
2. 服务端接收了用户的输入，将其作为 Web 应用模板内容的一部分，在进行目标编译渲染的过程中，执行了用户插入的恶意内容，因而可能导致了敏感信息泄露、代码执行等问题。其影响范围主要取决于模版引擎的复杂性，所以说 用户的输入永远都是不可信的，凡是使用模板的地方都可能会出现 SSTI 的问题，SSTI 不属于任何一种语言.

---

# SSTI 怎么产生的

**以 PHP Twig 为例**

- 正确写法 ✔
    ```php
    <?php
    require_once dirname(__FILE__).‘/../lib/Twig/Autoloader.php‘;
    Twig_Autoloader::register(true);

    $twig = new Twig_Environment(new Twig_Loader_String());
    $output = $twig->render("Hello {{name}}", array("name" => $_GET["name"]));  // 将用户输入作为模版变量的值
    echo $output;
    ```

    这段代码没有什么问题，用户的输入到时候渲染的时候就是 name 的值，由于 name 外面已经有 `{{}}` 了，也就是说，到时候显示的只是 name 变量的值，就算你输入了 `{{xxx}}` 输出也只是 `{{xxx}}` 而不会将 `xxx` 作为模板变量解析

    但是有些代码就是不这么写，比如下面这段代码

- 错误写法 ❌
    ```php
    <?php
    require_once dirname(__FILE__).‘/../lib/Twig/Autoloader.php‘;
    Twig_Autoloader::register(true);

    $twig = new Twig_Environment(new Twig_Loader_String());
    $output = $twig->render("Hello {$_GET[‘name‘]}");  // 将用户输入作为模版内容的一部分
    echo $output;
    ```

    现在开发者将用户的输入直接放在要渲染的字符串中了

    > 注意：不要把这里的 `{}` 当成是模板变量外面的括号，这里的括号实际上只是为了区分变量和字符串常量而已**，于是我们输入 `{{xxx}}` 就非常的符合模板的规则，模板引擎解析了，然后服务器就凉了。

**以 python 的 jinja2 为例**

- 错误写法1 ❌
    ```py
    @app.errorhandler(404)
    def page_not_found(e):
        template = '''{%% extends "layout.html" %%}
    {%% block body %%}
        <div class="center-content error">
            <h1>Oops! That page doesn't exist.</h1>
            <h3>%s</h3>
        </div>
    {%% endblock %%}
    ''' % (request.url)
        return render_template_string(template), 404
    ```

    这里使用了一个字符串的格式化来传递一个 url ，但是你别忘了你还是用模板的方式去渲染的啊，也就是说还是支持模板引擎支持的语法，那我们为什么不能输入模板引擎的语法呢？于是在 URL 后面跟上 `{{7+7}}` 自然而然就能计算出 49 了

- 错误写法2 ❌
    ```py
    # coding: utf-8
    import sys
    from jinja2 importTemplate

    template = Template("Your input: {}".format(sys.argv[1] if len(sys.argv) > 1 else '<empty>'))
    print template.render()
    ```

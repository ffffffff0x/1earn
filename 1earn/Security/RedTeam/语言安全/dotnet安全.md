# dotnet安全

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**教程**
- [aleenzz/.NET_study](https://github.com/aleenzz/.NET_study)

**案例**
- [越权漏洞反打钓鱼网站](https://www.t00ls.net/articles-58941.html)

---

## 反编译

**反编译工具**
- [dnSpy/dnSpy](https://github.com/dnSpy/dnSpy)
    - [dnSpyEx/dnSpy](https://github.com/dnSpyEx/dnSpy)
- [icsharpcode/ILSpy](https://github.com/icsharpcode/ILSpy)

---

## 简介

ASP.NET 开发可以选用两种框架：`ASP.NET Core` 与 `ASP.NET Framework`

ASP.NET 开发也分为两种：

**WebApplication**

WEB 应用程序，改变代码后需要重启网页。具有 namespace 空间名称，项目中所有的程序代码文件，和独立的文件都被编译成为一个程序集，保存在 bin 文件夹中。

**WebSite**

WEB 网站，改变代码后不用重启网页。它没用到 namespace 空间名称，每个 asp 页面会转成一个 dll。

### ASP.NET 的常见拓展名：

在 `%windir%\Microsoft.NET\Framework\v2.0.50727\CONFIG\web.config` 中有详细定义
- aspx：应用程序根目录或子目录，包含 web 控件与其他
- cs：类文件
- aspx.cs：web 窗体后台程序代码文件
- ascx：应用程序根目录或子目录, Web 用户控件文件。
- asmx：应用程序根目录或子目录，该文件包含通过 SOAP 方式可用于其他 Web 应用程序的类和方法。
- asax：应用程序根目录，通常是 Global.asax
- config：应用程序根目录或子目录，通常是 web.config
- ashx：应用程序根目录或子目录, 该文件包含实现 IHttpHandler 接口以处理所有传入请求的代码。
- soap: 应用程序根目录或子目录。soap 拓展文件

### 常见文件

**web.config**

1. web.config 是基于 XML 的文件，可以保存到 Web 应用程序中的任何目录中，这个文件包含了目录权限控制、数据库密码等等。

2. 加载方式：当前目录搜索 -> 上一级到根目录 -> `%windir%/Microsoft.NET/Framework/v2.0.50727/CONFIG/web.config` -> `%windir%/Microsoft.NET/Framework/v2.0.50727/CONFIG/machine.config` -> 都不存在返回 null

**Global.asax**

1. Global.asax 提供全局可用的代码，从 HttpApplication 基类派生的类，响应的是应用程序级别会话级别事件，通常 ASP.NET 的全局过滤代码就是在这里面。

**App_Data**

App_Data文件夹包含应用程序的本地数据存储

**bin**

包含应用程序所需的任何预生成的程序集

WEB 应用程序会把我们写的代码编译为 DLL 文件存放在 Bin 文件夹中，在 ASPX 中基本就是一些控件名，所以需要反编译他的 DLL 来进行审计。

例如 Logout.aspx
```c#
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Logout.aspx.cs" Inherits="Book.Logout" %>
```

在文件头中有这几个参数：

* Language="C#"  表示脚本语言
* AutoEventWireup="true" 表示是否自动关联某些特殊事件
* CodeBehind="Logout.aspx.cs" 表示指定包含与页关联的类的已编译文件的名称
* Inherits="Book.Logout" 表示定义供页继承的代码隐藏类

我们所关注的也就是 Inherits 的值，如上所示他指向了 Bin 目录下某个 dll 中 Book 类的 Logout 函数

---

## dotnet代码审计

### 逻辑漏洞

**ASP.NET 安全认证**

在 web.config 中有四种验证模式
* window - IIS 验证，在内联网环境中非常有用
* Passport - 微软集中式身份验证，一次登录便可访问所有成员站点，需要收费
* Form - 窗体验证，验证帐号 / 密码，Web 编程最佳最流行的验证方式
* None - 表示 ASP.NET 自己根本不执行身份验证，完全依赖 IIS 身份验证

开启 form 窗体验证的同时还需要配置 web.config，不然就会出现问题，一般来说还需要配置最基本的页面访问权限, 比如禁止匿名用户访问。
```ini
<system.web>
    <authorization>
    <deny users="?"/>
    </authorization>
</system.web>
```

当然还可以设置一些管理页面允许某某用户访问等等

除去web.config的配置通常还有两种写法来验证是否登陆。

第一种：在每个页面判断 `Session["UserName"]` 是否等于 null

第二种：类似 php 的 include 的继承，这也是本套程序使用的方法。

如果是没有任何验证的，也没有继承验证类的，无需登陆访问，这种就相当于是未授权了.

**认证绕过示例**

web.config
```xml
  <location path="purchase/orderdetail.aspx">
    <system.web>
      <authorization>
        <allow users="*"/>
      </authorization>
    </system.web>
  </location>

  <authentication mode="Forms" />
```

这里定义了 purchase/orderdetail.aspx 可以匿名访问 ，其中 `<authentication mode="Forms" />` 表示 Form 表单认证。

purchase/orderdetail.aspx
```c#
if (this.uid <= 0)
{
    if (!(base.Request.QueryString["g"] == "p"))
    {
        base.Response.Redirect("../login.aspx");
        return;
    }
    this.ph_pdf.Visible = false;
}
```

这里判断了参数 g

所以只需要访问 `purchase/orderdetail.aspx?g=p` 即可绕过跳转

**认证绕过示例2**

![](../../../../../assets/img/Security/RedTeam/语言安全/dotnet安全/dotnet代码审计/4.png)

在 23-26 行判断 `this.uid` 的值来进行跳转，在 16 行定义了他的值，跟进 `UserHelper.GetUserId`

```c#
public static int GetUserId
{
    get
    {
        if (Helper.IsUseAd && HttpContext.Current.Request.Cookies["userinfo"] == null)
        {
            UsersHelper.LoginAd(UserHelper.GetSamaccountName());
        }
        if (HttpContext.Current.Request.Cookies["userinfo"] != null)
        {
            return int.Parse(HttpContext.Current.Request.Cookies["userinfo"]["userid"]);
        }
        return -1;
    }
}
```

`this.uid` 等于 cookies 中获取的 `userinfo` 的值，这一步可以伪造，30-33 这里他设置了管理员的布尔值，跟进 `RoleHelper.IsAdmin`
```c#
public static bool IsAdmin
{
    get
    {
        string name = "IsAdmin";
        string admin = RoleHelper.Admin;
        bool? flag = HttpContext.Current.Session[name] as bool?;
        if (flag == null)
        {
            flag = new bool?(UserHelper.IsInAnyRoles(admin));
            HttpContext.Current.Session[name] = flag;
        }
        return flag.Value;
    }
}
```

前面从 session 中获取，如果 flag 为 null 则从 `UserHelper.IsInAnyRoles(admin)` 获取。

跟进 `IsInAnyRoles`

![](../../../../../assets/img/Security/RedTeam/语言安全/dotnet安全/dotnet代码审计/5.png)

可以看到只要我们传入的 cookies 中 roles 的等于传入的数组值就返回 true 其中 `public static string Admin = "administrators";`

所以构造 `cookies: userinfo=userid=1&roles=administrators;` 即可绕过认证

---

### 注入

**辅助工具**

* SQL Server Profiler

**漏洞示例1**

login.aspx
```c#
public void LoginForm()
{
    int num = UsersHelper.Login(this.txt_username.Text, this.txt_pwd.Text);
    if (num > 0)
    {
        base.Response.Redirect(FormsAuthentication.GetRedirectUrl(num.ToString(), true));
    }
    else
    {
        Helper.Result(this, "用户名或者密码错误");
    }
}
```

UsersHelper.Login
```c#
public static int Login(string username, string password)
{
    string sql = " select uid  from users_users where username=@username and password=@password;   ";
    SqlParameter[] prams = new SqlParameter[]
    {
        new SqlParameter("@username", username),
        new SqlParameter("@password", Helper.Encrypt(password))
    };
    object obj = Instance.ExeScalar(sql, prams);
    if (obj == null || obj == DBNull.Value)
    {
        return -1;
    }
    int num = int.Parse(obj.ToString());
    if (num > 0)
    {
        UsersHelper.Login(num);
    }
    return num;
}
```

注意,这里看上去像是存在注入,但其实使用采用了参数化查询,通过 SqlParameter 传递参数

search.aspx

![](../../../../../assets/img/Security/RedTeam/语言安全/dotnet安全/dotnet代码审计/1.png)

这里没有做处理,直接将参数与 text 拼接,然后传递给 ExeDataSet

![](../../../../../assets/img/Security/RedTeam/语言安全/dotnet安全/dotnet代码审计/2.png)

ExeDataSet 中对参数进行了 checkSql 但无任何处理,所以没有过滤，参数将被直接带入查询

> Payload: 1%' and 1=user--

**漏洞示例2**

![](../../../../../assets/img/Security/RedTeam/语言安全/dotnet安全/dotnet代码审计/3.png)

看到 69-88 行，存在 SQL 查询, 但要触发执行命令需要 this.isview 为 true

在 30-36 行赋值只需要 t=view 即可

sid 没有经过任何过滤，同时 ExeDataSet 函数也不存在过滤，即存在注入。

> Payload: purchase/orderdetail.aspx?g=p&t=view&sid=1%20and%201=user--

---

### XSS

**相关文章**
- [Request Validation - Preventing Script Attacks](https://docs.microsoft.com/en-us/aspnet/whitepapers/request-validation)

**validateRequest**

在 asp.net 中我们插入 XSS 代码经常会遇到一个错误 `A potentially dangerous Request.Form`

![](../../../../../assets/img/Security/RedTeam/语言安全/dotnet安全/dotnet代码审计/6.png)

这是因为在 aspx 文件头一般会定义一句 `<%@ Page validateRequest="true" %>` ，当然也可以在 web.config 中定义，值得注意的是 validateRequest 的值默认为 true , 所以通常情况下 asp.net 基本上是不存在 XSS 的, 除非程序员把他的值改变。

比如
```ini
<pages validateRequest="false" controlRenderingCompatibilityVersion="3.5" enableEventValidation="false">
    <controls>
    <add tagPrefix="pg" namespace="SiteUtils" assembly="DNHelper" />
    <add tagPrefix="pop" namespace="EeekSoft.Web" assembly="EeekSoft.Web.PopupWin" />
    <add tagPrefix="dnc" namespace="Dotnetcms.Controls" assembly="DNHelper" />
    <add tagPrefix="DayPilot" namespace="DayPilot.Web.Ui" assembly="DotnetControl" />
    </controls>
</pages>
```

---

### 文件上传

**分析案例**

```c#
private void SaveFile()
{
    string text = "../uploads/" + DateTime.Now.ToString("yyyy-MM") + "/";
    string text2 = HttpContext.Current.Server.MapPath(text);
    if (!Directory.Exists(text2))
    {
        Directory.CreateDirectory(text2);
    }
    HttpFileCollection files = HttpContext.Current.Request.Files;
    string fileName = Path.GetFileName(files[0].FileName);
    string extension = Path.GetExtension(files[0].FileName);
    string text3 = Helper.ReadConfigValue(Helper.ReadConfigXml("~/app_data/allow_ext.xml"), "allow_ext").ToString().ToLower();
    if (text3.Contains(extension.ToLower()))
    {
        string str = Guid.NewGuid().ToString() + extension;
        string filename = text2 + str;
        files[0].SaveAs(filename);
        string s = string.Concat(new string[]
        {
            "{\"jsonrpc\" : \"2.0\", \"result\" :\"",
            HttpContext.Current.Server.HtmlEncode(fileName),
            "\", \"id\" : \"",
            HttpContext.Current.Server.HtmlEncode(text + str),
            "\"}"
        });
        HttpContext.Current.Response.Write(s);
    }
}
```

文件名由 uploads + DateTime.Now.ToString("yyyy-MM") + Guid.NewGuid().ToString() + extension 组成

格式类似 `../uploads/2019-10/30777b5a-bd82-48eb-9104-24afffd97243.png`

所以能控制的只有 `extension`，他由 `Path.GetExtension` 直接获取文件后缀，但是 `ReadConfigXml` 读取 `~/app_data/allow_ext.xml` 的文件做比较，比较典型的白名单所以这里不存在任意文件上传。

allow_ext.xml
```xml
<?xml version="1.0" standalone="yes"?>
<PItems>
  <PItem Name="allow_ext" Value=".rar.zip.jpg.png.gif.doc.docx.xls.xlsx.ppt.pptx.jpeg.pdf" />
</PItems>
```

---

### 反序列化

**相关工具**
- [pwntester/ysoserial.net](https://github.com/pwntester/ysoserial.net)

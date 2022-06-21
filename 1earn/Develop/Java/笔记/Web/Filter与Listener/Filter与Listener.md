# Filter与Listener

---

在一些登录点或者是登录后才能使用的一些功能点里面，需要该用户登录后才去才能去访问或使用这些功能。但我们如果每个 servlet 都去进行一个判断是否登录，这些会有很多重复代码，而且效率也比较低。那么我们可以把这些代码都放到 Filter 过滤器里面去进行编写。

web 里面有三大组件：servlet、Filter、Listener。

---

## Filter 过滤器

filter 作用：当访问服务器的资源时，过滤器可以将请求拦截下来，完成一些特殊的功能。

在一个比较复杂的 Web 应用程序中，通常都有很多 URL 映射，对应的，也会有多个 Servlet 来处理 URL。

我们考察这样一个论坛应用程序：
```
            ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐
               /             ┌──────────────┐
            │ ┌─────────────>│ IndexServlet │ │
              │              └──────────────┘
            │ │/signin       ┌──────────────┐ │
              ├─────────────>│SignInServlet │
            │ │              └──────────────┘ │
              │/signout      ┌──────────────┐
┌───────┐   │ ├─────────────>│SignOutServlet│ │
│Browser├─────┤              └──────────────┘
└───────┘   │ │/user/profile ┌──────────────┐ │
              ├─────────────>│ProfileServlet│
            │ │              └──────────────┘ │
              │/user/post    ┌──────────────┐
            │ ├─────────────>│ PostServlet  │ │
              │              └──────────────┘
            │ │/user/reply   ┌──────────────┐ │
              └─────────────>│ ReplyServlet │
            │                └──────────────┘ │
             ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
```

各个 Servlet 设计功能如下：
- IndexServlet：浏览帖子；
- SignInServlet：登录；
- SignOutServlet：登出；
- ProfileServlet：修改用户资料；
- PostServlet：发帖；
- ReplyServlet：回复。

其中，ProfileServlet、PostServlet 和 ReplyServlet 都需要用户登录后才能操作，否则，应当直接跳转到登录页面。

我们可以直接把判断登录的逻辑写到这 3 个 Servlet 中，但是，同样的逻辑重复 3 次没有必要，并且，如果后续继续加 Servlet 并且也需要验证登录时，还需要继续重复这个检查逻辑。

为了把一些公用逻辑从各个 Servlet 中抽离出来，JavaEE 的 Servlet 规范还提供了一种 Filter 组件，即过滤器，它的作用是，在 HTTP 请求到达 Servlet 之前，可以被一个或多个 Filter 预处理，类似打印日志、登录检查等逻辑，完全可以放到 Filter 中。

我们编写一个最简单的 EncodingFilter，它强制把输入和输出的编码设置为 UTF-8：
```java
@WebFilter(urlPatterns = "/*")
public class EncodingFilter implements Filter {
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        System.out.println("EncodingFilter:doFilter");
        request.setCharacterEncoding("UTF-8");
        response.setCharacterEncoding("UTF-8");
        chain.doFilter(request, response);
    }
}
```

编写 Filter 时，必须实现 Filter 接口，在 `doFilter()` 方法内部，要继续处理请求，必须调用 `chain.doFilter()`。最后，用 `@WebFilter` 注解标注该 Filter 需要过滤的 URL。这里的 `/*` 表示所有路径。

添加了 Filter 之后，整个请求的处理架构如下：
```
            ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐
                                   /             ┌──────────────┐
            │                     ┌─────────────>│ IndexServlet │ │
                                  │              └──────────────┘
            │                     │/signin       ┌──────────────┐ │
                                  ├─────────────>│SignInServlet │
            │                     │              └──────────────┘ │
                                  │/signout      ┌──────────────┐
┌───────┐   │   ┌──────────────┐  ├─────────────>│SignOutServlet│ │
│Browser│──────>│EncodingFilter├──┤              └──────────────┘
└───────┘   │   └──────────────┘  │/user/profile ┌──────────────┐ │
                                  ├─────────────>│ProfileServlet│
            │                     │              └──────────────┘ │
                                  │/user/post    ┌──────────────┐
            │                     ├─────────────>│ PostServlet  │ │
                                  │              └──────────────┘
            │                     │/user/reply   ┌──────────────┐ │
                                  └─────────────>│ ReplyServlet │
            │                                    └──────────────┘ │
```

还可以继续添加其他 Filter，例如 LogFilter：
```java
@WebFilter("/*")
public class LogFilter implements Filter {
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        System.out.println("LogFilter: process " + ((HttpServletRequest) request).getRequestURI());
        chain.doFilter(request, response);
    }
}
```

多个 Filter 会组成一个链，每个请求都被链上的 Filter 依次处理：
```
                                        ┌────────┐
                                     ┌─>│ServletA│
                                     │  └────────┘
    ┌──────────────┐    ┌─────────┐  │  ┌────────┐
───>│EncodingFilter│───>│LogFilter│──┼─>│ServletB│
    └──────────────┘    └─────────┘  │  └────────┘
                                     │  ┌────────┐
                                     └─>│ServletC│
                                        └────────┘
```

有多个 Filter 的时候，Filter 的顺序如何指定？多个 Filter 按不同顺序处理会造成处理结果不同吗？

答案是 Filter 的顺序确实对处理的结果有影响。但遗憾的是，Servlet 规范并没有对 `@WebFilter` 注解标注的 Filter 规定顺序。如果一定要给每个 Filter 指定顺序，就必须在 `web.xml` 文件中对这些 Filter 再配置一遍。

注意到上述两个 Filter 的过滤路径都是 `/*`，即它们会对所有请求进行过滤。也可以编写只对特定路径进行过滤的 Filter，例如 AuthFilter：
```java
@WebFilter("/user/*")
public class AuthFilter implements Filter {
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        System.out.println("AuthFilter: check authentication");
        HttpServletRequest req = (HttpServletRequest) request;
        HttpServletResponse resp = (HttpServletResponse) response;
        if (req.getSession().getAttribute("user") == null) {
            // 未登录，自动跳转到登录页:
            System.out.println("AuthFilter: not signin!");
            resp.sendRedirect("/signin");
        } else {
            // 已登录，继续处理:
            chain.doFilter(request, response);
        }
    }
}
```

注意到 AuthFilter 只过滤以 `/user/` 开头的路径，因此：
* 如果一个请求路径类似 `/user/profile`，那么它会被上述 3 个 Filter 依次处理；
* 如果一个请求路径类似 `/test`，那么它会被上述 2 个 Filter 依次处理（不会被 `AuthFilter` 处理）。

再注意观察 `AuthFilter`，当用户没有登录时，在 `AuthFilter` 内部，直接调用 `resp.sendRedirect()` 发送重定向，且没有调用 `chain.doFilter()`，因此，当用户没有登录时，请求到达 `AuthFilter` 后，不再继续处理，即后续的 Filter 和任何 Servlet 都没有机会处理该请求了。

可见，Filter 可以有针对性地拦截或者放行 HTTP 请求。

如果一个 Filter 在当前请求中生效，但什么都没有做：
```java
@WebFilter("/*")
public class MyFilter implements Filter {
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // TODO
    }
}
```
那么，用户将看到一个空白页，因为请求没有继续处理，默认响应是 200 + 空白输出。

如果 Filter 要使请求继续被处理，就一定要调用 `chain.doFilter()` ！

---

定义步骤：

1. 定义一个类，实现接口Filter
2. 复写方法
3. 配置拦截路径

配置拦截路径有 2 种方式，分别是 web.xml 和注解进行配置。

### 注解配置拦截路径

```java
import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.IOException;

@WebFilter("/*")
public class FilerDemo1 implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {

    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        System.out.println("filterdemo执行");
        filterChain.doFilter(servletRequest, servletResponse);  //放行


    }

    @Override
    public void destroy() {

    }
}
```

### web.xml 配置拦截路径

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    <filter>
        <filter-name>demo1</filter-name>  //声明名字
        <filter-class>cn.test.web.filter.FilerDemo1</filter-class> //声明对应的filter过滤器
    </filter>

    <filter-mapping>
        <filter-name>demo1</filter-name>
        <url-pattern>/*</url-pattern>     //声明filter拦截资源
    </filter-mapping>
</web-app>
```

这里可以看到 filter 类，需要重写 3 个方法，这里的三个方法的作用分别是：

1. init: 在服务器启动后，会创建 Filter 对象，然后调用 init 方法。只执行一次。用于加载资源
2. doFilter: 每一次请求被拦截资源时，会执行。执行多次
3. destroy: 在服务器关闭后，Filter 对象被销毁。如果服务器是正常关闭，则会执行 destroy 方法。只执行一次。用于释放资源

服务器会先执行过滤器，再执行过滤器放行的资源，最好再执行过滤器放行后面的代码。

上面的代码直接拦截了所有的资源，定义的时候过滤器有多种的定义方式

1. 具体资源路径： /index.jsp   只有访问 index.jsp 资源时，过滤器才会被执行
2. 拦截目录： /user/*	访问 / user 下的所有资源时，过滤器都会被执行
3. 后缀名拦截： *.jsp		访问所有后缀名为 jsp 资源时，过滤器都会被执行
4. 拦截所有资源：/*		访问所有资源时，过滤器都会被执行

我们可以将后台的一些功能 servlet 定义为 amdin/addUserserlvlet, 定义多一层目录，拦截器可以直接定义拦截路径为 admin/* 这样，如果携带了登录的 session 后，才选择放行。

### 定义拦截方式

注解里面定义拦截路径，默认是 REQUEST 方式，也就是浏览器直接访问，使用转发或者或者是其他这些方式访问一样是会被拦截器给拦截的。

如果我们需要使用转发访问资源不被拦截器拦截，可以在注解中配置 dispatcherTypes 属性的值。

dispatcherTypes 五种属性：
1. REQUEST：默认值。浏览器直接请求资源
2. FORWARD：转发访问资源
3. INCLUDE：包含访问资源
4. ERROR：错误跳转资源
5. ASYNC：异步访问资源

代码：
```java
package cn.test.web.filter;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.IOException;

@WebFilter(value = "/*",dispatcherTypes = {DispatcherType.REQUEST,DispatcherType.FORWARD})  //定义浏览器请求和转发拦截器被执行
public class FilerDemo1 implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {

    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        System.out.println("filterdemo执行");
        filterChain.doFilter(servletRequest, servletResponse);  //放行


    }

    @Override
    public void destroy() {

    }
}
```

如果是在 web.xml 里面进行配置，那么我们只需要加入

REQUEST

web.xml 配置：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    <filter>
        <filter-name>demo1</filter-name>
        <filter-class>cn.test.web.filter.FilerDemo1</filter-class>
    </filter>

    <filter-mapping>
        <filter-name>demo1</filter-name>
        <url-pattern>/*</url-pattern>

        <dispatcher>REQUEST</dispatcher>
    </filter-mapping>

</web-app>
```

登陆过滤器案例：
```java
package cn.test.web.filter;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;

@WebFilter("/*")
public class loginFilter implements Filter {
    public void destroy() {
    }

    public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain) throws ServletException, IOException {
            System.out.println(req);
            //强制转换成 HttpServletRequest
            HttpServletRequest request = (HttpServletRequest) req;

            //获取资源请求路径
            String uri = request.getRequestURI();
            //判断是否包含登录相关资源路径,排除掉 css/js/图片/验证码等资源
            if(uri.contains("/login.jsp") || uri.contains("/loginServlet") || uri.contains("/css/") || uri.contains("/js/") || uri.contains("/fonts/") || uri.contains("/checkCodeServlet")  ){
                //包含，用户就是想登录。放行
                chain.doFilter(req, resp);
            }else{
                //不包含，需要验证用户是否登录
                //从获取session中获取user
                Object user = request.getSession().getAttribute("user");
                if(user != null){
                    //登录了。放行
                    chain.doFilter(req, resp);
                }else{
                    //没有登录。跳转登录页面

                    request.setAttribute("login_msg","您尚未登录，请登录");
                    request.getRequestDispatcher("/login.jsp").forward(request,resp);
                }
            }

            // chain.doFilter(req, resp);
        }

    public void init(FilterConfig config) throws ServletException {

    }

}
```

---

### 修改请求

Filter 可以对请求进行预处理，因此，我们可以把很多公共预处理逻辑放到 Filter 中完成。

考察这样一种需求：我们在 Web 应用中经常需要处理用户上传文件，例如，一个 UploadServlet 可以简单地编写如下：
```java
@WebServlet(urlPatterns = "/upload/file")
public class UploadServlet extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 读取Request Body:
        InputStream input = req.getInputStream();
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        byte[] buffer = new byte[1024];
        for (;;) {
            int len = input.read(buffer);
            if (len == -1) {
                break;
            }
            output.write(buffer, 0, len);
        }
        // TODO: 写入文件:
        // 显示上传结果:
        String uploadedText = output.toString(StandardCharsets.UTF_8);
        PrintWriter pw = resp.getWriter();
        pw.write("<h1>Uploaded:</h1>");
        pw.write("<pre><code>");
        pw.write(uploadedText);
        pw.write("</code></pre>");
        pw.flush();
    }
}
```

是要保证文件上传的完整性怎么办？如果在上传文件的同时，把文件的哈希也传过来，服务器端做一个验证，就可以确保用户上传的文件一定是完整的。

这个验证逻辑非常适合写在 ValidateUploadFilter 中，因为它可以复用。

我们先写一个简单的版本，快速实现ValidateUploadFilter的逻辑：
```java
@WebFilter("/upload/*")
public class ValidateUploadFilter implements Filter {

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        HttpServletRequest req = (HttpServletRequest) request;
        HttpServletResponse resp = (HttpServletResponse) response;
        // 获取客户端传入的签名方法和签名:
        String digest = req.getHeader("Signature-Method");
        String signature = req.getHeader("Signature");
        if (digest == null || digest.isEmpty() || signature == null || signature.isEmpty()) {
            sendErrorPage(resp, "Missing signature.");
            return;
        }
        // 读取Request的Body并验证签名:
        MessageDigest md = getMessageDigest(digest);
        InputStream input = new DigestInputStream(request.getInputStream(), md);
        byte[] buffer = new byte[1024];
        for (;;) {
            int len = input.read(buffer);
            if (len == -1) {
                break;
            }
        }
        String actual = toHexString(md.digest());
        if (!signature.equals(actual)) {
            sendErrorPage(resp, "Invalid signature.");
            return;
        }
        // 验证成功后继续处理:
        chain.doFilter(request, response);
    }

    // 将byte[]转换为hex string:
    private String toHexString(byte[] digest) {
        StringBuilder sb = new StringBuilder();
        for (byte b : digest) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    // 根据名称创建MessageDigest:
    private MessageDigest getMessageDigest(String name) throws ServletException {
        try {
            return MessageDigest.getInstance(name);
        } catch (NoSuchAlgorithmException e) {
            throw new ServletException(e);
        }
    }

    // 发送一个错误响应:
    private void sendErrorPage(HttpServletResponse resp, String errorMessage) throws IOException {
        resp.setStatus(HttpServletResponse.SC_BAD_REQUEST);
        PrintWriter pw = resp.getWriter();
        pw.write("<html><body><h1>");
        pw.write(errorMessage);
        pw.write("</h1></body></html>");
        pw.flush();
    }
}
```

`ValidateUploadFilter` 对签名进行验证的逻辑是没有问题的，但是，`UploadServlet` 并未读取到任何数据！

这里的原因是对 `HttpServletRequest` 进行读取时，只能读取一次。如果 Filter 调用 `getInputStream()` 读取了一次数据，后续 Servlet 处理时，再次读取，将无法读到任何数据。怎么办？

这个时候，我们需要一个 “伪造” 的 `HttpServletRequest`，具体做法是使用代理模式，对 `getInputStream()` 和 `getReader()` 返回一个新的流：
```java
class ReReadableHttpServletRequest extends HttpServletRequestWrapper {
    private byte[] body;
    private boolean open = false;

    public ReReadableHttpServletRequest(HttpServletRequest request, byte[] body) {
        super(request);
        this.body = body;
    }

    // 返回InputStream:
    public ServletInputStream getInputStream() throws IOException {
        if (open) {
            throw new IllegalStateException("Cannot re-open input stream!");
        }
        open = true;
        return new ServletInputStream() {
            private int offset = 0;

            public boolean isFinished() {
                return offset >= body.length;
            }

            public boolean isReady() {
                return true;
            }

            public void setReadListener(ReadListener listener) {
            }

            public int read() throws IOException {
                if (offset >= body.length) {
                    return -1;
                }
                int n = body[offset] & 0xff;
                offset++;
                return n;
            }
        };
    }

    // 返回Reader:
    public BufferedReader getReader() throws IOException {
        if (open) {
            throw new IllegalStateException("Cannot re-open reader!");
        }
        open = true;
        return new BufferedReader(new InputStreamReader(new ByteArrayInputStream(body), "UTF-8"));
    }
}
```

注意观察 `ReReadableHttpServletRequest` 的构造方法，它保存了 `ValidateUploadFilter` 读取的 `byte[]` 内容，并在调用 `getInputStream()` 时通过 `byte[]` 构造了一个新的 ServletInputStream。

然后，我们在 `ValidateUploadFilter` 中，把 `doFilter()` 调用时传给下一个处理者的 `HttpServletRequest` 替换为我们自己 “伪造” 的 `ReReadableHttpServletRequest`：
```java
public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
        throws IOException, ServletException {
    ...
    chain.doFilter(new ReReadableHttpServletRequest(req, output.toByteArray()), response);
}
```

再注意到我们编写 ReReadableHttpServletRequest 时，是从 HttpServletRequestWrapper 继承，而不是直接实现 HttpServletRequest 接口。这是因为，Servlet 的每个新版本都会对接口增加一些新方法，从 HttpServletRequestWrapper 继承可以确保新方法被正确地覆写了，因为 HttpServletRequestWrapper 是由 Servlet 的 jar 包提供的，目的就是为了让我们方便地实现对 HttpServletRequest 接口的代理。

我们总结一下对 `HttpServletRequest` 接口进行代理的步骤：

1. 从 `HttpServletRequestWrapper` 继承一个 `XxxHttpServletRequest`，需要传入原始的 `HttpServletRequest` 实例；
2. 覆写某些方法，使得新的 `XxxHttpServletRequest` 实例看上去 “改变” 了原始的 `HttpServletRequest` 实例；
3. 在 `doFilter()` 中传入新的 `XxxHttpServletRequest` 实例。

虽然整个 Filter 的代码比较复杂，但它的好处在于：这个 Filter 在整个处理链中实现了灵活的 “可插拔” 特性，即是否启用对 Web 应用程序的其他组件（Filter、Servlet）完全没有影响。

### 修改响应

既然我们能通过 `Filter` 修改 `HttpServletRequest`，自然也能修改 HttpServletResponse，因为这两者都是接口。

我们来看一下在什么情况下我们需要修改 HttpServletResponse。

假设我们编写了一个 Servlet，但由于业务逻辑比较复杂，处理该请求需要耗费很长的时间：
```java
@WebServlet(urlPatterns = "/slow/hello")
public class HelloServlet extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        resp.setContentType("text/html");
        // 模拟耗时1秒:
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
        }
        PrintWriter pw = resp.getWriter();
        pw.write("<h1>Hello, world!</h1>");
        pw.flush();
    }
}
```

好消息是每次返回的响应内容是固定的，因此，如果我们能使用缓存将结果缓存起来，就可以大大提高 Web 应用程序的运行效率。

缓存逻辑最好不要在 Servlet 内部实现，因为我们希望能复用缓存逻辑，所以，编写一个 CacheFilter 最合适：
```java
@WebFilter("/slow/*")
public class CacheFilter implements Filter {
    // Path到byte[]的缓存:
    private Map<String, byte[]> cache = new ConcurrentHashMap<>();

    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        HttpServletRequest req = (HttpServletRequest) request;
        HttpServletResponse resp = (HttpServletResponse) response;
        // 获取Path:
        String url = req.getRequestURI();
        // 获取缓存内容:
        byte[] data = this.cache.get(url);
        resp.setHeader("X-Cache-Hit", data == null ? "No" : "Yes");
        if (data == null) {
            // 缓存未找到,构造一个伪造的Response:
            CachedHttpServletResponse wrapper = new CachedHttpServletResponse(resp);
            // 让下游组件写入数据到伪造的Response:
            chain.doFilter(request, wrapper);
            // 从伪造的Response中读取写入的内容并放入缓存:
            data = wrapper.getContent();
            cache.put(url, data);
        }
        // 写入到原始的Response:
        ServletOutputStream output = resp.getOutputStream();
        output.write(data);
        output.flush();
    }
}
```

实现缓存的关键在于，调用 `doFilter()` 时，我们不能传入原始的 `HttpServletResponse`，因为这样就会写入 Socket，我们也就无法获取下游组件写入的内容。如果我们传入的是 “伪造” 的 `HttpServletResponse`，让下游组件写入到我们预设的 `ByteArrayOutputStream`，我们就 “截获” 了下游组件写入的内容，于是，就可以把内容缓存起来，再通过原始的 `HttpServletResponse` 实例写入到网络。

这个 `CachedHttpServletResponse` 实现如下：
```java
class CachedHttpServletResponse extends HttpServletResponseWrapper {
    private boolean open = false;
    private ByteArrayOutputStream output = new ByteArrayOutputStream();

    public CachedHttpServletResponse(HttpServletResponse response) {
        super(response);
    }

    // 获取Writer:
    public PrintWriter getWriter() throws IOException {
        if (open) {
            throw new IllegalStateException("Cannot re-open writer!");
        }
        open = true;
        return new PrintWriter(output, false, StandardCharsets.UTF_8);
    }

    // 获取OutputStream:
    public ServletOutputStream getOutputStream() throws IOException {
        if (open) {
            throw new IllegalStateException("Cannot re-open output stream!");
        }
        open = true;
        return new ServletOutputStream() {
            public boolean isReady() {
                return true;
            }

            public void setWriteListener(WriteListener listener) {
            }

            // 实际写入ByteArrayOutputStream:
            public void write(int b) throws IOException {
                output.write(b);
            }
        };
    }

    // 返回写入的byte[]:
    public byte[] getContent() {
        return output.toByteArray();
    }
}
```

可见，如果我们想要修改响应，就可以通过 `HttpServletResponseWrapper` 构造一个 “伪造” 的 `HttpServletResponse`，这样就能拦截到写入的数据。

修改响应时，最后不要忘记把数据写入原始的 `HttpServletResponse` 实例。

这个 `CacheFilter` 同样是一个 “可插拔” 组件，它是否启用不影响 Web 应用程序的其他组件（Filter、Servlet）。

---

## Listener 监听器

除了 Servlet 和 Filter 外，JavaEE 的 Servlet 规范还提供了第三种组件：Listener。

事件监听机制：
* 事件	：一件事情
* 事件源 ：事件发生的地方
* 监听器 ：一个对象
* 注册监听：将事件、事件源、监听器绑定在一起。 当事件源上发生某个事件后，执行监听器代码

Listener 顾名思义就是监听器，有好几种 Listener，其中最常用的是 `ServletContextListener`，我们编写一个实现了 `ServletContextListener` 接口的类如下：
```java
@WebListener
public class AppListener implements ServletContextListener {
    // 在此初始化WebApp,例如打开数据库连接池等:
    public void contextInitialized(ServletContextEvent sce) {
        System.out.println("WebApp initialized.");
    }

    // 在此清理WebApp,例如关闭数据库连接池等:
    public void contextDestroyed(ServletContextEvent sce) {
        System.out.println("WebApp destroyed.");
    }
}
```

任何标注为 `@WebListener`，且实现了特定接口的类会被 Web 服务器自动初始化。上述 `AppListener` 实现了 `ServletContextListener` 接口，它会在整个 Web 应用程序初始化完成后，以及 Web 应用程序关闭后获得回调通知。我们可以把初始化数据库连接池等工作放到 `contextInitialized()` 回调方法中，把清理资源的工作放到 `contextDestroyed()` 回调方法中，因为 Web 服务器保证在 `contextInitialized()` 执行后，才会接受用户的 HTTP 请求。

很多第三方 Web 框架都会通过一个 `ServletContextListener` 接口初始化自己。

除了 `ServletContextListener` 外，还有几种 Listener：

* HttpSessionListener：监听 HttpSession 的创建和销毁事件；
* ServletRequestListener：监听 ServletRequest 请求的创建和销毁事件；
* ServletRequestAttributeListener：监听 ServletRequest 请求的属性变化事件（即调用 `ServletRequest.setAttribute()` 方法）；
* ServletContextAttributeListener：监听 ServletContext 的属性变化事件（即调用 `ServletContext.setAttribute()` 方法）；

### ServletContext

一个 Web 服务器可以运行一个或多个 WebApp，对于每个 WebApp，Web 服务器都会为其创建一个全局唯一的 `ServletContext` 实例，我们在 `AppListener` 里面编写的两个回调方法实际上对应的就是 `ServletContext` 实例的创建和销毁：

```java
public void contextInitialized(ServletContextEvent sce) {
    System.out.println("WebApp initialized: ServletContext = " + sce.getServletContext());
}
```

`ServletRequest`、`HttpSession` 等很多对象也提供 `getServletContext()` 方法获取到同一个 `ServletContext` 实例。`ServletContext` 实例最大的作用就是设置和共享全局信息。

此外，`ServletContext` 还提供了动态添加 Servlet、Filter、Listener 等功能，它允许应用程序在运行期间动态添加一个组件，虽然这个功能不是很常用。

---

## Source & Reference

- https://www.cnblogs.com/nice0e3/p/13551701.html
- https://www.liaoxuefeng.com/wiki/1252599548343744/1266264823560128

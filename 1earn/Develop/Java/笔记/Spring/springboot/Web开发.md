# Web开发

---

## Thymeleaf

静态资源访问

在我们开发 Web 应用的时候，需要引用大量的 js、css、图片等静态资源。Spring Boot 默认提供静态资源目录位置需置于 classpath 下，目录名需符合如下规则：
- /static
- /public
- /resources
- /META-INF/resources

举例：我们可以在 src/main/resources/ 目录下创建 static，在该位置放置一个图片文件。启动程序后，尝试访问 http://localhost:8080/D.jpg。如能显示图片，配置成功。

新建一个 Spring Boot 应用，在 pom.xml 中加入所需的模板引擎模块，比如使用 thymeleaf 的话，只需要引入下面依赖：
```xml
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

创建一个 Spring MVC 的传统 Controller，用来处理根路径的请求，将解决渲染到 index 页面上，具体实现如下
```java
@Controller
public class HelloController {

    @GetMapping("/")
    public String index(ModelMap map) {
        map.addAttribute("host", "http://www.abc.com");
        return "index";
    }

}
```

简要说明：
- 在渲染到 index 页面的时候，通过 ModelMap，往页面中增加一个 host 参数，其值为 http://www.abc.com
- return 的值 index 代表了要使用的模板页面名称，默认情况下，它将对应到 src/main/resources/templates / 目录下的 index.html 模板页面

根据上一步要映射的模板，去模板路径 src/main/resources/templates 下新建模板文件 index.html，内容如下：
```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8" />
    <title></title>
</head>
<body>
<h1 th:text="${host}">Hello World</h1>
</body>
</html>
```

在该页面的 body 中，包含了一个带有 Thymeleaf 属性的 h1 标签，该便签内容将绑定 host 参数的值。

由于 Thymeleaf 通过属性绑定的特性。该模板页面同其他模板引擎不同，直接通过浏览器打开 html 页面，它是可以正常运作的，将会直接展现 Hello World 标题。这有利于开发页面的时候可以在非启动环境下验证应前端样式的正确性。

如果启动程序后，访问http://localhost:8080/

**Thymeleaf 的配置参数**

如有需要修改默认配置的时候，只需复制下面要修改的属性到 application.properties 中，并修改成需要的值：
```conf
# Enable template caching.
spring.thymeleaf.cache=true
# Check that the templates location exists.
spring.thymeleaf.check-template-location=true
# Content-Type value.
spring.thymeleaf.content-type=text/html
# Enable MVC Thymeleaf view resolution.
spring.thymeleaf.enabled=true
# Template encoding.
spring.thymeleaf.encoding=UTF-8
# Comma-separated list of view names that should be excluded from resolution.
spring.thymeleaf.excluded-view-names=
# Template mode to be applied to templates. See also StandardTemplateModeHandlers.
spring.thymeleaf.mode=HTML5
# Prefix that gets prepended to view names when building a URL.
spring.thymeleaf.prefix=classpath:/templates/
# Suffix that gets appended to view names when building a URL.
spring.thymeleaf.suffix=.html  spring.thymeleaf.template-resolver-order= # Order of the template resolver in the chain. spring.thymeleaf.view-names= # Comma-separated list of view names that can be resolved.
```

举几个我们常用的配置内容：

- 不想每次修改页面都重启

    修改 spring.thymeleaf.cache 参数，设置为 false

- 不想使用 template 目录存放模板文件

    修改 spring.thymeleaf.prefix 参数，设置为你想放置模板文件的目录

- 不想使用 index 作为模板文件的扩展名

    修改 spring.thymeleaf.suffix 参数，设置为你想用的扩展名

- HTML5 的严格校验很烦人

    修改 spring.thymeleaf.mode 参数，设置为 LEGACYHTML5

---

## ECharts

ECharts是百度开源的一个前端组件。它是一个使用 JavaScript 实现的开源可视化库，可以流畅的运行在 PC 和移动设备上，兼容当前绝大部分浏览器（IE8/9/10/11，Chrome，Firefox，Safari等），底层依赖矢量图形库 ZRender，提供直观，交互丰富，可高度个性化定制的数据可视化图表。

它提供了常规的折线图、柱状图、散点图、饼图、K线图，用于统计的盒形图，用于地理数据可视化的地图、热力图、线图，用于关系数据可视化的关系图、treemap、旭日图，多维数据可视化的平行坐标，还有用于 BI 的漏斗图，仪表盘，并且支持图与图之间的混搭。

除了已经内置的包含了丰富功能的图表，ECharts 还提供了自定义系列，只需要传入一个renderItem函数，就可以从数据映射到任何你想要的图形，更棒的是这些都还能和已有的交互组件结合使用而不需要操心其它事情。

在resources/templates目录下创建index.html页面
```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8" />
    <title>Spring Boot中使用ECharts</title>
    <script src="https://cdn.bootcss.com/echarts/4.6.0/echarts.min.js"></script>
</head>
<body>
<div id="main" style="width: 1000px;height:400px;"></div>
</body>

<script type="text/javascript">
    // 初始化ECharts组件到id为main的元素上
    let myChart = echarts.init(document.getElementById('main'));
    // 定义图标的配置项
    let option = {
        title: {
            text: 'Spring Boot中使用ECharts'
        },
        tooltip: {},
        // x轴配置
        xAxis: {
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        // y轴配置
        yAxis: {},
        series: [{
            // 数据集（也可以从后端的Controller中传入）
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            // 图表类型，这里使用line，为折线图
            type: 'line'
        }]
    };
    myChart.setOption(option);
</script>
</html>
```

在页面内容中主要包含三部分：
- `<head>` 中通过 `<script>` 标签引入 ECharts 的组件 JS，这里使用了 bootcss 的免费公共 cdn。如果用于自己生产环境，不建议使用这类免费 CDN 的 JS 或者 CSS 等静态资源。可以从官网下载所需的静态内容，放到 Spring Boot 的静态资源位置（如果不知道在哪，可见上一篇），或是放到自己公司的静态资源管理的服务器上，实现动静分离。
- `<body>` 中定义了一个 id 为 main 的 `<div>` 标签，这个标签后续将用来渲染 EChart 组件
- 最后的一段 `<script>` 内容则是具体的 EChart 图标的展现初始化和配置。具体配置内容可见代码中的注释信息。

启动应用，访问 localhost:8080，如果上面操作均无差错，那就会得到折线图

---

## 文件上传

在pom.xml中引入模版引擎依赖：
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```
你也可以选择其他你熟悉的模版引擎，比如：Freemarker。

在resources目录下，创建新目录templates；在templates目录下再创建一个文件上传的页面upload.html，内容如下：
```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8" />
    <title>文件上传页面</title>
</head>
<body>
<h1>文件上传页面</h1>
<form method="post" action="/upload" enctype="multipart/form-data">
    选择要上传的文件：<input type="file" name="file"><br>
    <hr>
    <input type="submit" value="提交">
</form>
</body>
</html>
```

创建文件上传的处理控制器，命名为UploadController
```java
@Controller
@Slf4j
public class UploadController {

    @Value("${file.upload.path}")
    private String path;

    @GetMapping("/")
    public String uploadPage() {
        return "upload";
    }

    @PostMapping("/upload")
    @ResponseBody
    public String create(@RequestPart MultipartFile file) throws IOException {
        String fileName = file.getOriginalFilename();
        String filePath = path + fileName;

        File dest = new File(filePath);
        Files.copy(file.getInputStream(), dest.toPath());
        return "Upload file success : " + dest.getAbsolutePath();
    }

}
```

其中包含这几个重要元素：
- 成员变量 path，通过 @Value 注入配置文件中的 file.upload.path 属性。这个配置用来定义文件上传后要保存的目录位置。
- GET 请求，路径 /，用于显示 upload.html 这个文件上传页面。
- POST 请求。路径 /upload，用于处理上传的文件，即：保存到 file.upload.path 配置的路径下面。

编辑application.properties配置文件
```conf
spring.servlet.multipart.max-file-size=2MB
spring.servlet.multipart.max-request-size=2MB

file.upload.path=/Users/didi/
```

前两个参数用于限制了上传请求和上传文件的大小，而file.upload.path是上面我们自己定义的用来保存上传文件的路径。

---

## Source & Reference

- [Spring Boot 2.x基础教程：使用 Thymeleaf开发Web页面](https://blog.didispace.com/spring-boot-learning-21-4-1/)
- [Spring Boot 2.x基础教程：使用 ECharts 绘制各种华丽的数据图表](https://blog.didispace.com/spring-boot-learning-21-4-2/)
- [Spring Boot 2.x基础教程：实现文件上传](https://blog.didispace.com/spring-boot-learning-21-4-3/)

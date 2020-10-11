
**方法一：Form表单提交**

html代码：
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>上传文件</title>
  <script src="Scripts/jquery-1.11.3.min.js"></script>
</head>
<body>
  <form action="UploadHandler.ashx" method="post" enctype="multipart/form-data">
    <input id="file_upload" name="file_upload" type="file" />
    <input id="btn_upload" type="submit" value="上传" />
  </form>
</body>
</html>
```

UploadHandler.ashx代码：
```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApplication1
{
  /// <summary>
  /// UploadHandler 的摘要说明
  /// </summary>
  public class UploadHandler : IHttpHandler
  {
    public void ProcessRequest(HttpContext context)
    {
      context.Response.ContentType = "text/plain";

      HttpPostedFile file = context.Request.Files["file_upload"];
      string filePath = context.Server.MapPath("~/UploadFiles/") + System.IO.Path.GetFileName(file.FileName);
      file.SaveAs(filePath);

      context.Response.Write("上传文件成功");
    }

    public bool IsReusable
    {
      get
      {
        return false;
      }
    }
  }
}
```

该方法虽然能够实现文件的上传，但是form表单提交之后整个页面就刷新了，如果要无刷新上传文件的话，就要使用ajax了。

**方法二：jquery + ajax无刷上传**

html代码：
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>上传文件</title>
  <script src="Scripts/jquery-1.11.3.min.js"></script>
</head>
<body>
  <input id="file_upload" name="file_upload" type="file" />
  <input id="btn_upload" type="button" value="上传" />

  <script>
    $(document).ready(function ()
    {
      $('#btn_upload').bind('click', function ()
      {
        var formData = new FormData();
        formData.append('upload_file', $('#file_upload')[0].files[0]);
        $.ajax({
          url: 'UploadHandler.ashx',
          type: 'post',
          data: formData,
          contentType: false,
          processData: false,
          success: function (msg)
          {
            if (msg == "Yes")
            {
              alert('文件上传成功');
            }
            else
            {
              alert('文件上传失败');
            }
          }
        })
      });
    });
  </script>
</body>
</html>
```

UploadHandler.ashx代码：
```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApplication1
{
  /// <summary>
  /// UploadHandler 的摘要说明
  /// </summary>
  public class UploadHandler : IHttpHandler
  {

    public void ProcessRequest(HttpContext context)
    {
      context.Response.ContentType = "text/plain";

      if (context.Request.Files.Count > 0)
      {
        HttpPostedFile file = context.Request.Files["upload_file"];
        string filePath = context.Server.MapPath("~/UploadFiles/") + System.IO.Path.GetFileName(file.FileName);
        file.SaveAs(filePath);
        context.Response.Write("Yes");
      }
      else
      {
        context.Response.Write("No");
      }
    }

    public bool IsReusable
    {
      get
      {
        return false;
      }
    }
  }
}
```

**Source & Reference**
- [利用ashx文件实现文件的上传功能](https://blog.csdn.net/HerryDong/article/details/100549765)

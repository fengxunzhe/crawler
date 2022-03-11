## 一、内存漫游原理
      1、客户端 --->>> 服务器  【正常操作】
      
               anyproxy
      2、客户端 --->>> 服务器：
         客户端 与 服务器 交互数据时，相当于anyproxy把数据流量截取下来，windows有fiddler,MAC有charles
         
## 二、环境搭建[相当于fiddler安装ca证书]
      1、npm install -g anyproxy express body-parser shelljs crypto cheerio @babel/core @babel/types @babel/generator   # -g代表安装在npm的全局
      
      2、anyproxy ca # 同fiddler抓取https也要安装证书一样，anyproxy安装 在cmd下安装 
![imag](https://github.com/fengxunzhe/crawler/blob/main/%E5%86%85%E5%AD%98%E6%BC%AB%E6%B8%B8/img/1.png)

      3、Http proxy started on port 8001 # 启动后将终端http代理服务器配置为ip:8001
         web interface started on port 8002 # web界面上能看到所有的请求信息ip:8002
         
      4、打开网页访问 127.0.0.1:8002,安装证书
![imag](https://github.com/fengxunzhe/crawler/blob/main/%E5%86%85%E5%AD%98%E6%BC%AB%E6%B8%B8/img/2.png)
![imag](https://github.com/fengxunzhe/crawler/blob/main/%E5%86%85%E5%AD%98%E6%BC%AB%E6%B8%B8/img/3.png)
![imag](https://github.com/fengxunzhe/crawler/blob/main/%E5%86%85%E5%AD%98%E6%BC%AB%E6%B8%B8/img/4.png)

## 三、原理
      1、访问目标网站时，经过我们的自定义代理服务器anyproxy，截获流量
      
      2、对于流量中的JS 和 HTML代码，使用AST处理，注入HOOK逻辑
      
      3、

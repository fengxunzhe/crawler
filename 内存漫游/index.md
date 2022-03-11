## 一、内存漫游原理
      1、客户端 --->>> 服务器  【正常操作】
      
               anyproxy
      2、客户端 --->>> 服务器：
         客户端 与 服务器 交互数据时，相当于anyproxy把数据hook下来，修改 在放行
         
## 二、环境搭建
      1、npm install -g anyproxy express body-parser shelljs crypto cheerio @babel/core @babel/types @babel/generator   # -g代表安装在npm的全局
      
      2、anyproxy ca # 同fiddler抓取https也要安装证书一样，anyproxy安装 在cmd下安装
      
            


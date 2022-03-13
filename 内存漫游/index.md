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
      ===1、访问目标网站时，经过我们的自定义代理服务器anyproxy，截获流量(通过127.0.0.1:8002可打开anyproxy查看)
      
           1.1、自定义AnyProxy，实现拦截流量
                  const AnyProxy = require('anyproxy')
                  const option = {
                      port: 8001, // 非网页端拦截的端口
                      // rule: require('myRuleModule'),  // 拦截的规则
                      webInterface:{
                          enable: true,
                          webPort: 8002  //网页端拦截的端口
                      },
                      throttle: 10000,    // 速率
                      forceProxyHttps: false, // 是否强制拦截https
                      wsIntercept: false,  // 是否拦截websocket
                      silent: false,  // 是否console.log打印到控制台
                      systemProxy: true // 自定义参数
                  };
                  if(option.systemProxy){  // 是否开启代理
                      AnyProxy.utils.systemProxyMgr.enableGlobalProxy('127.0.0.1', option.port)
                  }
                  const proxyServer = new AnyProxy.ProxyServer(option);

                  proxyServer.on('ready',() => { /* */ })  // 代理成功开启后，做什么操作
                  proxyServer.on('error',() => { /* */ })  // 代理开启失败后，做什么操作


                  // 插件：局部代理
                  // 全局代理，所有应用都走的

                  proxyServer.start() // 代理开启

                  // proxyServer.close()
                  
            1.2、全局代理 和  非全局代理
             
                  开启全局代理后，关掉需要在以下中关掉
![imag](https://github.com/fengxunzhe/crawler/blob/main/%E5%86%85%E5%AD%98%E6%BC%AB%E6%B8%B8/img/5.png)
                  
                  局部代理，使用谷歌SwitchyOmega
![imag](https://github.com/fengxunzhe/crawler/blob/main/%E5%86%85%E5%AD%98%E6%BC%AB%E6%B8%B8/img/7.png) 
            
            1.3、使用演示
                  开启全局代理后：webPort: 8002  //网页端拦截的端口 
                  打开网页访问127.0.0.1:8002，即可查看到经过的数据流量
![imag](https://github.com/fengxunzhe/crawler/blob/main/%E5%86%85%E5%AD%98%E6%BC%AB%E6%B8%B8/img/6.png)     

                  开启谷歌局部代理: 流量走我们的anyproxy代理服务器
![imag](https://github.com/fengxunzhe/crawler/blob/main/%E5%86%85%E5%AD%98%E6%BC%AB%E6%B8%B8/img/8.png) 
      
      ===2、对于流量中的JS 和 HTML代码，使用AST处理，注入HOOK逻辑
      
            2.1、 规则过滤 rule: require('myRuleModule'),  // 拦截的规则
                  ①、拦截并修改正在发送的请求
                        包括请求头(request header)、请求头(request body)，甚至请求的目标地址
                  ②、拦截并修改服务端响应
                        包括http状态码(status code)、响应头(response header)、响应内容(response content)
                  ③、拦截修改https请求
                        本质是中间人攻击、需要客户端提取信任CA证书    
            2.2、rule文件
            
                  module.exports = {  // 我们自己写模块的时候，需要在模块最后写好模块接口，声明这个模块对外暴露什么内容，module.exports 提供了暴露接口的方法
                      summary: 'test rule module for AnyProxy', // 模块介绍

                      *beforeSendRequest(requestDetail){},   // 自定义方法  发送请求前拦截处理

                      *beforeSendResponse(requestDetail, responseDetail){},  // 自定义方法  发送响应前拦截处理

                      *beforeDealHttpsRequest(){},  // 自定义方法  是否处理https请求

                      *onError(requestDetail, error){},  // 自定义方法  处理请求出错的事件

                      *onConnectError(requestDetail, error){}   //// 自定义方法  处理HTTPS连接服务器出错
                  }
                  
                  单个案例：
                    *beforeSendResponse(requestDetail, responseDetail){
                    console.log("-------------",requestDetail.url)
                    if(requestDetail.url.indexOf("bbs")>=0){     //  判断请求的链接是否有baidu关键字
                        const newResponse = responseDetail.response;  //取出返回结果
                        newResponse.body = '----------------Test--------------';  // 更改返回结果为==========Test===========
                        return {
                            response: newResponse
                        }  // 返回response，此处返回的必须是一对键值
                    }
                    return {  //判断请求的链接是否有baidu关键字,没有的话放行
                        response: responseDetail.response
                    }
                },

      3、
      


## 目的：找kg_dfid加密算法
![imag](https://github.com/fengxunzhe/crawler/blob/main/kugou/img/1-1.png)

## 实战
#### 1、通过全局搜索定位到加密点
![imag](https://github.com/fengxunzhe/crawler/blob/main/kugou/img/1-2.png)

#### 2、kg_dfid = t ； t = e.data.dfid ;

#### 3、e 是通过ajax发送一个post请求，成功返回的一个对象
![imag](https://github.com/fengxunzhe/crawler/blob/main/kugou/img/1-3.png)

#### 4、更明显一点  e是该post请求生成，所以首先要模拟该post请求，但是参数是加密的，通过上文可知data:s
![imag](https://github.com/fengxunzhe/crawler/blob/main/kugou/img/1-4.png)

#### 5、s = CryptoJS.enc.Base64.stringify(l); var l = CryptoJS.enc.Utf8.parse(t);  t = JSON.stringify(e); 所以需要找传入的e是什么

## 1、通过抓包发现参数：kg_mid数据加密,cookies中kg_mid正有该值，so抓取cookies中kg_mid值

## 2、通过搜索kg_mid，定位到cookie中生成的地方：如下

![imag](https://github.com/fengxunzhe/crawler/blob/main/kugou/img/1.png)

#### 首先先明白google调试的三个按钮作用：
①、跳过该JS函数,比如某个参数是该JS函数生成的，但是并不是我们想要的，我们可以点跳过,那么会继续执行下个参数是生成的函数

②、跳过该函数,比如我们进入到某个函数内部，但是单步执行很慢，我们可以直接跳过该函数

③、单步进入，进入函数内部，一步步执行
 ![imag](https://github.com/fengxunzhe/crawler/blob/main/kugou/img/66.png)
 

## 3、单步进入write 函数，定位到cookie写入的位置，取消之前的断点，此处下断点，点击跳过函数,直到e = kg_mid 点击单步进入

 ![imag](https://github.com/fengxunzhe/crawler/blob/main/kugou/img/2.png)
4、单步进入到生成kg_mid的函数，查看堆栈，定位到上一步生成的位置如下：
-
 ![imag](https://github.com/fengxunzhe/crawler/blob/main/kugou/img/3.png)
5、通过堆栈，定位到生成的位置
-
 ![imag](https://github.com/fengxunzhe/crawler/blob/main/kugou/img/4.png)
6、定位到加密点
-
 ![imag](https://github.com/fengxunzhe/crawler/blob/main/kugou/img/5.png)

1、通过抓包发现参数：kg_mid数据加密,cookies中kg_mid正有该值，so抓取cookies中kg_mid值
-
2、通过搜索kg_mid，定位到cookie中生成的地方：如下
-
 ![imag](https://github.com/fengxunzhe/crawler/blob/main/kugou/img/1.png)

3、单步进入write 函数，定位到cookie写入的位置，取消之前的断点，此处下断点
-

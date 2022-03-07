
【现象】在爬取 实习僧 招聘网站时；对应的字体乱码  https://www.shixiseng.com/interns?keyword=python&page=1&city=%E5%85%A8%E5%9B%BD&type=intern
    <a href="https://www.shixiseng.com/intern/inn_lfezezr0rzt5?pcm=pc_SearchList" title="&#xf2af&#xe185&#xe447&#xf45b&#xe491&#xf77b实习&#xedb9" target="_blank" 
    class="title ellipsis font" data-v-98c756d6="">实习</a>

######  方法一  #####硬钢法：把每个字体对应的字符拷贝出来
  如：title="&#xf2af&#xe185&#xe447&#xf45b&#xe491&#xf77b实习&#xedb9"   title对应的本应该是"python实习生"  
       &#xf2af&#xe185&#xe447&#xf45b&#xe491&#xf77b实习&#xedb9  看个数 p正好对应&#xf2af   y对应的是&#xe185  依次类推
   
  源码：
        import requests
        
        from bs4 import BeautifulSoup

        baseURL = "https://www.shixiseng.com/interns?keyword=python&page=1&city=%E5%85%A8%E5%9B%BD&type=intern"

        resp = requests.get(baseURL)

        bs = BeautifulSoup(resp.text, 'lxml')

        bs_list = bs.select('div.intern-wrap.intern-item div.clearfix.intern-detail div.f-l.intern-detail__job p a')
        for i in bs_list:
            title = i['title'].replace('&#xf2af', 'p').replace('&#xe185', 'y').\
                replace('&#xe447', 't').replace('&#xf45b', 'h').\
                replace('&#xe491', 'o').replace('&#xf77b', 'n').\
                replace('&#xedb9', '生').replace('&#xf8d9', 'P')

            print(title)
       ====================输出结果================
               Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
                runfile('C:/Users/AF/PycharmProjects/pythonProject3/test2.py', wdir='C:/Users/AF/PycharmProjects/pythonProject3')
                Python&#xe33d&#xf1c2&#xef59
                python实习生
                python实习生
                python爬虫实习生
                Python&#xe33d&#xf1c2&#xef59实习生
                Python实习生
                Python开发实习
                Python实习生
                Python开发&#xe33d&#xf1c2&#xef59
                python开发&#xe33d&#xf1c2&#xef59
                Python研发&#xe33d&#xf1c2&#xef59
                Python开发实习生
                

######  方法二  #####字体文件映射法

        1、通过F12开发者工具检测字体的CSS格式如下
            .font[data-v-98c756d6] {
                font-family: myFont;
            }
            
        2、通过在源码中搜索 myFont 可知道 字体文件所在https://www.shixiseng.com/interns/iconfonts/file?rand=0.9295410685101846
             @font-face {    font-family: myFont;    src: url(/interns/iconfonts/file?rand=0.9295410685101846);}
        
        3、该字体文件是.tff格式的，通过字体查看工具FontCreator可打开该文件，查看字体映射表
        
        4、pip install FontTools 通过python的开源包操作
        
        5、任务：①、xml文件中0xe084  对应的汉字编码是  uni8F6F，而通过源码获取到的是&#xe33d  需要将&#全部替换成0
                ②、将替换后的0xe084格式全部替换成找到的 uni8F6F
        <cmap>
            <tableVersion version="0"/>
            <cmap_format_4 platformID="0" platEncID="3" language="0">
              <map code="0x78" name="x"/><!-- LATIN SMALL LETTER X -->
              <map code="0xe084" name="uni8F6F"/><!-- ???? -->
              <map code="0xe094" name="uni44"/><!-- ???? -->
              <map code="0xe0ab" name="uni884C"/><!-- ???? -->
              <map code="0xe0e4" name="uni65"/><!-- ???? -->
              <map code="0xe157" name="uni4E8C"/><!-- ???? -->
              <map code="0xe16b" name="uni8BBE"/><!-- ???? -->
              <map code="0xe185" name="uni79"/><!-- ???? -->

=====================================================
        一、需要将&#全部替换成0
                import requests
                from bs4 import BeautifulSoup

                baseURL = "https://www.shixiseng.com/interns?keyword=python&page=1&city=%E5%85%A8%E5%9B%BD&type=intern"

                resp = requests.get(baseURL)

                bs = BeautifulSoup(resp.text, 'lxml')

                bs_list = bs.select('div.intern-wrap.intern-item div.clearfix.intern-detail div.f-l.intern-detail__job p a')
                for i in bs_list:
                    title = i['title'].replace('&#', '0')
                    print(title)
                    
                    #  0xf8d90xe1850xe4470xf45b0xe4910xf77b开发0xe33d0xf1c20xef59
                    #  0xf2af0xe1850xe4470xf45b0xe4910xf77b开发0xe33d0xf1c20xef59
                    #  0xf8d90xe1850xe4470xf45b0xe4910xf77b研发0xe33d0xf1c20xef59
                    
            
        二、将替换后的0xe084格式全部替换成找到的 uni8F6F
            1、获取xml文件中的映射关系
                import requests

                # 下载字体文件
                myFont = requests.get('https://www.shixiseng.com/interns/iconfonts/file?rand=0.9295410685101846')
                with open('file.ttf', 'wb') as f:
                    f.write(myFont.content)

                print("---")

                from fontTools.ttLib import TTFont
                font = TTFont('./file.ttf') # <fontTools.ttLib.ttFont.TTFont object at 0x0000025CAFC56A30>
                font.saveXML('font.xml')

                # 获取xml中的映射关系
                bestcmap = font['cmap'].getBestCmap()  # 57476: 'uni8F6F', 57492: 'uni44', 57515: 'uni884C', 57572: 'uni65'
                newDict = {}
                for k, v in bestcmap.items(): # 获取key value 保存在newDict中
                    newDict[hex(k)] = v
                
                此时newDict中的key value 是这种格式 0xe094: 'uni8F6F', 0xe185: 'uni44', 0xe185: 'uni884C', 0xe185: 'uni65'
                
                然后将  以下全部替换成         uni8F6F 这种            
                    #  0xf8d90xe1850xe4470xf45b0xe4910xf77b开发0xe33d0xf1c20xef59
                    #  0xf2af0xe1850xe4470xf45b0xe4910xf77b开发0xe33d0xf1c20xef59
                    #  0xf8d90xe1850xe4470xf45b0xe4910xf77b研发0xe33d0xf1c20xef59
    
    
                import requests
                from bs4 import BeautifulSoup

                baseURL = "https://www.shixiseng.com/interns?keyword=python&page=1&city=%E5%85%A8%E5%9B%BD&type=intern"

                resp = requests.get(baseURL)

                bs = BeautifulSoup(resp.text, 'lxml')

                bs_list = bs.select('div.intern-wrap.intern-item div.clearfix.intern-detail div.f-l.intern-detail__job p a')
                for i in bs_list:
                    title = i['title'].replace('&#', '0')
                    
                    for k, v in newDic.items():
                        title.replace(k，v) # 把 0xf8d90xe1850xe4470xf45b0xe4910xf77b研发0xe33d0xf1c20xef59 替换成 uni884Cuni884Cuni884Cuni884C这种
                    
                    for k，v in xxx: # 最后一步，替换成真实文字
               
               最后通过fontCreator工具可以看到真实文件对应的uni884 Cuni884Cuni884Cuni884C这种 值是多少，最后进行替换即可
                    




        

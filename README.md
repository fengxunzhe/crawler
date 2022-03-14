# crawler
反爬虫技巧学习

### 1、windows 和 global的区别
      在浏览器中, window是用来"兜底"的对象, 所有默认定义的对象都是window的子对象；而在node.js中没有window, 对等关系的是global
      所以我们在node.js中要使用windows对象的属性时：
      可以这样
      window = global
      
      后面我们就可以使用wwindow的属性
        closed	返回窗口是否已被关闭。
        defaultStatus	设置或返回窗口状态栏中的默认文本。
        【document	对 Document 对象的只读引用。(请参阅对象)】
        frames	返回窗口中所有命名的框架。该集合是 Window 对象的数组，每个 Window 对象在窗口中含有一个框架。
        history	对 History 对象的只读引用。请参数 History 对象。
        innerHeight	返回窗口的文档显示区的高度。
        innerWidth	返回窗口的文档显示区的宽度。
        localStorage	在浏览器中存储 key/value 对。没有过期时间。
        length	设置或返回窗口中的框架数量。
        【location	用于窗口或框架的 Location 对象。请参阅 Location 对象。】
        name	设置或返回窗口的名称。
        【navigator	对 Navigator 对象的只读引用。请参数 Navigator 对象。】
        opener	返回对创建此窗口的窗口的引用。
        outerHeight	返回窗口的外部高度，包含工具条与滚动条。
        outerWidth	返回窗口的外部宽度，包含工具条与滚动条。
        pageXOffset	设置或返回当前页面相对于窗口显示区左上角的 X 位置。
        pageYOffset	设置或返回当前页面相对于窗口显示区左上角的 Y 位置。
        parent	返回父窗口。
        screen	对 Screen 对象的只读引用。请参数 Screen 对象。
        screenLeft	返回相对于屏幕窗口的x坐标
        screenTop	返回相对于屏幕窗口的y坐标
        screenX	返回相对于屏幕窗口的x坐标
        sessionStorage	在浏览器中存储 key/value 对。 在关闭窗口或标签页之后将会删除这些数据。
        screenY	返回相对于屏幕窗口的y坐标
        self	返回对当前窗口的引用。等价于 Window 属性。
        status	设置窗口状态栏的文本。
        top	返回最顶层的父窗口。

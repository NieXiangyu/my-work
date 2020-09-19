# 新人的工作记录

## [学习日志]

### 2020/7/5-2020/7/11

  熟悉看linux/Windows操作系统命令行参数写成的教程，简单熟悉Markdown,Git用法  
  安装虚拟机失败，网上的安装教程很多却没有一个解决了实际安装问题，准备回学校后安装双系统  
  
### 2020/7/12-2020/7/18  

  完成[在线实验平台](https://course.educg.net)上ROS教程1，初步了解ROS  
  正在看 Launchviz 部分内容，先看作图部分  
  
### 2020/7/19-2020/7/25

学习现状：学习graphviz，以便自己看懂代码，但是看教程困难重重。

#### 2020/7/21会议内容 
 1.解决graphviz安装使用问题  
[graphviz安装使用问题](https://github.com/NieXiangyu/my-work/blob/master/graphviz%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8%E9%97%AE%E9%A2%98.md)  
 2.分配任务。我的任务：Launchviz工具中分析ARG参数，分析python相关的message      
 3.简要讲解graph.py代码，任务：添加注释     
 
 #### 2020/7/23晚小会议
 参会人：聂翔宇，周智维     
 1.解决我看graph.py代码遇到的一些细节问题：不知道engine,attr，node等含义以及用法，类的初始化方法
    解决方法：分清graphviz软件与graphviz包的区别。      
    graphviz软件介绍见官网：http://www.graphviz.org/  
    graphviz包介绍见官网：https://graphviz.readthedocs.io/en/stable/   
 2.讲解代码注释应有的写法格式：  
   '''        
      :param 参数 :参数含义     
      :type 参数 :参数类型      
      :return :    
      :rtype :(后两个说明返回参数含义与类型）     
           
   '''      
  3.说明graph.py代码中定义的1,2,3,101,等数字与官方已下载包与类型的要求无关，只是自己定义    
  
  #### 2020/7/30晚小会议
 参会人：聂翔宇，周智维，赵作竑  
 1.解决我在Ubuntu虚拟机（ https://course.educg.net/ 在线平台）上问题运行 https://github.com/Alexzhoucs/AV-Arch-analyzing-tool.git 中的测试文件时问题   
   问题：运行时显示No module named 'graphviz',但是写的dot文件成功画出了图  
   解决方法：虽然已经通过apt-get install graphviz命令安装了软件，却没有pip install graphviz安装相关包，输入命令安装包即可解决，在Ubuntu上比要上官网下载的windows上便利    
 2. 运行时产生python3兼容问题, python3运行ros方法报错： No module named 'rospkg'      
    原因：ROS默认支持 Python2，而Launchviz使用python3开发，故使用 Python3 运行会报错找不到 rospkg 包。    
    解决： 更新 `pip3` 后按[此教程](https://blog.csdn.net/weixin_43046653/article/details/102930894)操作即可解决       
          主要是安装三个相关支持包  
            ```    
            $ sudo apt install python3-pip   
            $ sudo pip3 install rospkg   
            $ sudo pip3 install netifaces   
            $ sudo pip3 install defusedxml   
            ``` 
        小插曲：中途运行sudo pip3 install rospkg 时连接国外网站被墙，速度极慢。
        解决：在文件/etc/apt/source.listd/中将国外网站链接变为[科大镜像](http://mirrors.ustc.edu.cn/)网站上ros中源地址，将软件源添加至系统，详情：      
        http://mirrors.ustc.edu.cn/help/ros.html      
       
 3. 引导我使用已有launchviz程序画简单图，定下目标：熟悉整个工具，进行注释，完全看懂代码后目标分析参数并改进。对Launchviz增加对launch文件中参数的分析。
 
  ### 2020/7/26-2020/8/1  
   #### 2020/7/31晚小会议
   参会人：聂翔宇，周智维，张老师  
   内容：指导我看analyzer.py和file.py代码的一部分，简单讲解xml文件含义，引导我查阅官方文档，布置小任务。   
   
  学习情况：看懂了代码Graph.py已经附属程序，完成graphvis的作图练习，学会了用graphviz以及周智维代码Graph.py作图。   
  目标:    熟悉xml文件，解析launch文件参数  
  正在进行:  阅读解析文件部分代码analyzer.py和file.py，这部分耗时较久，无论是xml文件还是DOM对象都不太懂   
  计划: 1.完成小任务： 编写程序提取并输出launch文件中arg元素的属性name和default的值，结合官方文档弄懂代码。       
        2.试着改进代码  
 资料链接：[xml.dom官方文档](https://docs.python.org/2/library/xml.dom.minidom.html)  
          [xml.etree.ElementTree官方文档](https://docs.python.org/2/library/xml.etree.elementtree.html#module-xml.etree.ElementTree)   
          [Python XML 解析](https://www.runoob.com/python/python-xml.html)     
          [XML DOM 教程](https://www.runoob.com/dom/dom-tutorial.html)   
          [XML教程](https://www.runoob.com/xml/xml-tutorial.html)   
          
 
 ### 2020/8/2-2020/8/8  
   [XML学习要点总结](https://github.com/NieXiangyu/my-work/blob/master/XML%E5%AD%A6%E4%B9%A0%E8%A6%81%E7%82%B9%E6%80%BB%E7%BB%93)     
   #### 2020/8/2晚线上小会议  
   参会人：聂翔宇，周智维，张老师    
   目标:  熟悉xml文件，解析launch文件参数  
   done:  完成编写程序提取并输出launch文件中arg元素的属性name和default的值的小任务，熟悉了xml.dom.minium与xml.etree.ElementTree的用法    
   [任务完成代码,xml.dom.minidom方式]:(https://github.com/NieXiangyu/my-work/blob/master/my_analysis.py)               
   [任务完成代码,xml.etree.ElementTree方式]:(https://github.com/NieXiangyu/my-work/blob/master/my_analysis.py)                    
   todo:  1.继续深入学习launch(xml)文件解析有关内容，学习roslaunch与 rospkg.common有关内容，以求完全读懂analyzer.py和file.py   
           2.完成小任务：编写程序，找出launch文件中参数$使用部分，对使用情况进行总结，参考教程：http://wiki.ros.org/roslaunch/XML  
          
   #### 2020/8/5下午小会议  
   参会人：聂翔宇，周智维  
   目标：解析launch文件参数，读懂并改进Launchviz部分  
   done: 完成任务：编写程序，找出launch文件中$(arg参数使用部分与被引用位置，与参数定义关联起来，输出定义参数所在文件中行号。任务调用xml.sax部分完成，同时初步完成xml.sax部分学习  
   Todo: 弄懂Launchviz中context（nake_context调用了roslaunch与rospkg）的含义，梳理总结context的含义与形成过程。编写程序输出单个文件的context   
   
   [xml.sax官方文档]：(https://docs.python.org/3/library/xml.sax.html)        
   [xml.sax相关教程]：(https://www.jianshu.com/p/9c9802ab4989)       
   [任务完成代码]: (https://github.com/NieXiangyu/my-work/blob/master/my_find_arg.py)        
   
   说明：程序查找了arg定义所在行号与$(arg 出现语句所在行号。此处行号从<launch>开始算第一行，且无视空行，每读一个元素行号的计数+1。      
   实现方式：xml.sax.ContentHandler部分的分析方法是一个一个元素读取，无视子节点关系，每读取一次行号计数+1，故没有内容的空行不会记录，所以打开文件左边的行号与此处计数不一致。     
   要得到直观上看上去文件中行号（相当于当做.txt文件处理），直接f.readlines(),f.writelines()计数，但是这样体现不出xml文件结构特点，暂时不完成，因为觉得应该没有此需求，有需求之后考虑完成。

 ### 2020/8/9-2020/8/15

   #### 2020/8/13 下午会议   
   参会人：聂翔宇，周智维，张老师    
   内容：说明arg参数分析需求，简要说明launch文件rosparam,param参数含义。   
   确定目标：返校之后在笔记本电脑上配置好所有文件后运行Launchviz示例。    

### 2020/9/14-2020/9/19
   完成：安装 Turtlebot，[参考教程]:(https://github.com/S4Plus/ABC/blob/master/ROS/Turtlebot.md)            
   [安装Turtlebot问题与解决]：(https://github.com/NieXiangyu/my-work/blob/master/%E5%AE%89%E8%A3%85Tuetlebot%E9%97%AE%E9%A2%98%E4%B8%8E%E8%A7%A3%E5%86%B3)
     

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
     学习情况：看懂了代码Graph.py已经附属程序，完成graphvis的作图练习，学会了用graphviz以及周智维代码Graph.py作图。   
     目标:    熟悉xml文件，解析launch文件参数  
     正在进行:  阅读解析文件部分代码analyzer.py和file.py，这部分耗时较久，无论是xml文件还是DOM对象都不太懂   
     计划: 1.完成小任务： 编写程序提取并输出launch文件中arg元素的属性name和default的值，结合官方文档弄懂代码。       
           2.试着改进代码    

      

 
   
   
    
    
 




   
   
   
   

 


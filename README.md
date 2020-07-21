# 新人的工作记录

## [学习日志]

### 2020/7/5-2020/7/11
  熟悉看linux/Windows操作系统命令行参数写成的教程，简单熟悉Markdown,Git用法
  安装虚拟机失败，网上的安装教程很多却没有一个解决了实际安装问题，准备回学校后安装双系统
  
### 2020/7/12-2020/7/18  
  完成[在线实验平台](https://course.educg.net)上ROS教程1，初步了解ROS
  正在看 Launchviz 部分内容，先看作图部分
  
### 2020/7/19-2020/7/25
   1.现状：学习graphviz，以便自己看懂代码，但是看教程困难重重。[教程：十分钟学会graphviz画图](https://www.jianshu.com/p/6d9bbbbf38b1)
   2.问题一：系统路径
   安装在任意喜欢的位置。但是需要把安装目录的graphviz\bin加入环境变量PATH里，环境变量配置：
   桌面计算机右键“属性”→高级系统设置→环境变量→系统变量Path后分号加入graphviz\bin文件完整路径名（其实安装是可以设置加入，不过被杀毒软件阻止了）
   3.问题二：运行文件时（输入dot -Tpng first.dot -o first.png），显示Format: "pdf" not recognized。
   解决方法：https://gitlab.com/graphviz/graphviz/-/issues/1315
   即终端输入dot.exe -c，之后就正常了。（至少我是这样的）
   
   
   
   

 


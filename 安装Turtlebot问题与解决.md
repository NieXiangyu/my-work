[安装参考教程](https://github.com/S4Plus/ABC/blob/master/ROS/Turtlebot.md)    
问题语句：rosdep install --from-paths src -i -y    
输入时问题：   
![](./image/problem2.png)    
尝试加上--allow-unauthenticated,结果：     
![](./image/problem3.png)
![](./image/problem4.png)
查百度，解决方案：    
![](./image/problem5.png)
尝试过后，rosdep install --from-paths src -i -y 还是不行   
解决方法：输入rosdep install --from-paths src -i，之后安装时一直点Y(yes)，麻烦一些而已。          

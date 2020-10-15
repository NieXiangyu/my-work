1.创建工作空间
运行如下命令：

$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make

结果：出现文件夹catkin_ws，内有build,devel,src三个文件夹

2.将要运行的文件夹(如param_test)复制到src文件夹中（已含有CMakeLists.tst）

3.运行source devel/setup.bash，再运行echo $ROS_PACKAGE_PATH，以确保显示/home/youruser/catkin_ws/src:/opt/ros/kinetic/share，表示catkin_ws包在路径内

4.先用roscore命令启动ros，可以输入 roscore &在后台运行,ctrl+z暂停运行输入其他命令，ctrl+C为结束命令。

5.输入rosrun package_name executable_file_name 或 roslaunch package_name launch_file_name

（如：rosrun param_test paramtest test1.launch 或 roslaunch param_test test2.launch ）

对比：使用rosrun之前，我们一定得需要启动rosmaster，即开启一个窗口输入roscore，rosrun是运行一个单独节点的命令，如果要运行多个节点，则需要使用多次rosrun命令；

而roslaunch采用XML的格式对需要运行的节点进行描述，可以同时运行多个节点，且可以不用输入，如果我们没有开一个terminal跑`roscore`,运行roslaunch文件后rosmaster会自动启动．当然你关闭了roslaucn之后rosmaster也会关闭。

6.运行时：

前台运行程序：ctrl+c结束运行，ctrl+z暂停运行

暂停运行程序：fg转入前台运行，bg转入后台运行

后台运行程序：fg转入前台运行




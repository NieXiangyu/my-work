sudo命令以系统管理者的身份执行指令，也就是说，经由 sudo 所执行的指令就好像是 root 亲自执行。使用权限：在 /etc/sudoers 中有出现的使用者。

参数说明：
-V 显示版本编号
-h 会显示版本编号及指令的使用方式说明
-l 显示出自己（执行 sudo 的使用者）的权限

$ sudo [-u username] [command]

-u：将身份变成username的身份



 su:是最简单的身份切换名，用su我们能够进行不论什么用户的切换，一般都是su - username，然后输入password就ok了，可是root用su切换到其它身份的时候是不须要输入password的。一般我们切换身份都是切换到root，然后进行一些仅仅有root能干的事，比方改动配置文件。比方下载安装软件。这些都仅仅能是root才有权限干的事。切换到root能够是单纯的su，或者是su -和su - root，后面两个是一样的意思。 单纯使用su切换到root，读取变量的方式是non-login shell，这样的方式下非常多的变量都不会改变。尤其是PATH。所以root用的非常多的命令都仅仅能用绝对路径来运行。这样的方式仅仅是切换到root的身份。

而用su -这样的方式的话，是login shell方式，它是先以root身份登录然后再运行别的操作。

 假设我们仅仅要切换到root做一次操作就好了，仅仅要在su后面加个-c參数就好了。运行完这次操作后。又会自己主动切换回我们自己的身份。

区别：sudo仅仅是须要自己的password，就能够以其它用户的身份来运行命令。常常是以root的身份运行命令。



apt命令：一般需要获得root，所以一般在前边加上sudo，一般格式为sudo apt-get xxx。（下文中packagename指代为软件包的名称。）
apt-get update
在修改/etc/apt/sources.list或/etc/apt/preferences之后运行该命令。需要定期运行这一命令以确保您的软件包列表是最新的。
apt-get install packagename
安装一个新软件包（与下文的aptitude功能类似）
apt-get remove packagename
卸载一个已安装的软件包（保留配置文档）
apt-get remove --purge packagename
卸载一个已安装的软件包（删除配置文档），注意“--”符号必不可少



`dpkg` :即 package manager for Debian ，是 Debian 和基于 Debian 的系统中一个主要的**包管理工具**，可以用来安装、构建、卸载、管理 `deb` 格式的软件包。

使用 `dpkg` 命令安装软件时，可以使用 `-i` 选项并指定 deb 安装包的路径。和 apt-get有所不同:
 `apt-get` 命令并不直接操作 deb 安装包文件，而是从 `/etc/apt/sources.list` 配置文件中定义的软件镜像源里下载软件包并安装，使用时也只需指定软件的名称（或者也可以附加上版本号）。

apt-get 命令安装软件：
 `$ apt-get install <package_name[=version]>`

dpkg 命令安装软件：
 `$ dpkg -i <package_file_path>`

因此，dpkg 主要是用来安装已经下载到本地的 deb 软件包，或者对已经安装好的软件进行管理。而 apt-get 可以直接从远程的软件仓库里下载安装软件。

可以使用 `dpkg -l` 命令列出当前系统中已经安装的软件以及软件包的**状态**。

`dpkg` 命令的 `-r` 选项可以用来卸载已安装的软件包，此时只需要指定软件的名称即可。

查看软件包的内容:dpkg -c <package_file_path>

查看软件包（已安装）的详细信息 : `dpkg -s <package>`或  `dpkg --status <package> `

查看软件包的安装位置: `dpkg -L <package>` 或 `dpkg --list-files <package>`
筛选出包含指定文件（模式）的软件包:`dpkg -S <filename_pattern> `或 `dpkg --search <filename_pattern>`



 wget是一个下载文件的工具，它用在命令行下。 

wget支持HTTP，HTTPS和FTP协议，可以使用HTTP代理。所谓的自动下载是指，wget可以在用户退出系统的之后在后台执行。这意味这你可以登录系统，启动一个wget下载任务，然后退出系统，wget将在后台执行直到任务完成

  wget 可以跟踪HTML页面上的链接依次下载来创建远程服务器的本地版本，完全重建原始站点的目录结构。这又常被称作”递归下载”。



cd：cd命令用来切换工作目录至dirname。 其中dirName表示法可为绝对路径或相对路径。(cd = Change Directory) 

cd .. 跳至上层目录

cd ../../  跳至上上层目录

cd ~/     跳入用户主目录

cd -  跳入上次使用目录

pwd：pwd命令以绝对路径的方式显示用户当前工作目录。(pwd = print working Directory) 

mkdir：mkdir命令用来创建目录。该命令创建由dirname命名的目录。如果在目录名的前面没有加任何路径名，则在当前目录下创建由dirname指定的目录；
如果给出了一个已经存在的路径，将会在该目录下创建一个指定的目录。在创建目录时，应保证新建的目录与它所在目录下的文件没有重名。
参数：-p：在创建目录时，保证dirName中的目录的存在，若不存在则创建对应的目录

ls（英文全拼：list files）命令用于显示指定工作目录下之内容（列出目前工作目录所含之文件及子目录)。
参数 :-a 显示所有文件及目录 (ls内定将文件名或目录名称开头为"."的视为隐藏档，不会列出)
     -l 除文件名称外，亦将文件型态、权限、拥有者、文件大小等资讯详细列出

rm（英文全拼：remove）命令用于删除一个文件或者目录。
参数 :-i 删除前逐一询问确认。
     -f 即使原档案属性设为唯读，亦直接删除，无需逐一确认。
     -r 将目录及以下之档案亦逐一删除。

cp（英文全拼：copy file）命令主要用于复制文件或目录。
参数：-a：此选项通常在复制目录时使用，它保留链接、文件属性，并复制目录下的所有内容。其作用等于dpR参数组合。
    -d：复制时保留链接。这里所说的链接相当于Windows系统中的快捷方式。
    -f：覆盖已经存在的目标文件而不给出提示。
    -i：与-f选项相反，在覆盖目标文件之前给出提示，要求用户确认是否覆盖，回答"y"时目标文件将被覆盖。
    -p：除复制文件的内容外，还把修改时间和访问权限也复制到新文件中。
    -r：若给出的源文件是一个目录文件，此时将复制该目录下所有的子目录和文件。(常用，用户使用该指令复制目录时，必须使用参数-r或者-R)
    -l：不复制文件，只是生成链接文件。
eg:使用指令 cp 将当前目录 test/ 下的所有文件复制到新目录 newtest 下，输入如下命令：cp –r test/ newtest

source命令：
source命令也称为“点命令”，也就是一个点符号（.）,是bash的内部命令。
功能：使Shell读入指定的Shell程序文件并依次执行文件中的所有语句
source命令通常用于重新执行刚修改的初始化文件，使之立即生效，而不必注销并重新登录。
用法：
source filename 或 . filename
source命令(从 C Shell 而来)是bash shell的内置命令;点命令(.)，就是个点符号(从Bourne Shell而来)是source的另一名称。
source filename 与 sh filename 及./filename执行脚本的区别在那里呢？
1.当shell脚本具有可执行权限时，用sh filename与./filename执行脚本是没有区别得。./filename是因为当前目录没有在PATH中，所有"."是用来表示当前目录的。
2.sh filename 重新建立一个子shell，在子shell中执行脚本里面的语句，该子shell继承父shell的环境变量，但子shell新建的、改变的变量不会被带回父shell，除非使用export。
3.source filename：这个命令其实只是简单地读取脚本里面的语句依次在当前shell里面执行，没有建立新的子shell。那么脚本里面所有新建、改变变量的语句都会保存在当前shell里面。

sh命令：是shell命令语言解释器，执行命令从标准输入读取或从一个文件中读取。通过用户输入命令，和内核进行沟通
参数：-c	     命令从-c后的字符串读取
            -i      实现脚本交互
           -n      进行shell脚本的语法检查
            -x      实现shell脚本逐条语句的跟踪 

echo命令:功能是在显示器上显示一段文字，一般起到一个提示的作用。
该命令的一般格式为： echo [ -n ] 字符串
参　　 数：-n 不要在最后自动换行(具体用法较多）

cat（英文全拼：concatenate）命令:用于连接文件并打印到标准输出设备上。
参数说明：https://www.runoob.com/linux/linux-comm-cat.html

任务调度命令：
jobs命令：可以用来查看当前终端放入后台的工作，工作管理的名字也来源于 jobs 命令。
jobs 命令常用选项及含义：
-l（L 的小写） 	列出进程的 PID 号。
-n 	只列出上次发出通知后改变了状态的进程。
-p 	只列出进程的 PID 号。
-r 	只列出运行中的进程。
-s 	只列出已停止的进程。

bg：将一个在后台暂停的命令，变成继续执行

fg：将后台中的命令调至前台继续运行

ps命令(Process Status):用来列出系统中当前运行的那些进程。ps命令列出的是当前那些进程的快照，就是执行ps命令的那个时刻的那些进程.
如果想要动态的显示进程信息，就可以使用top命令。

history:记录执行过的命令。history [n]  n为数字，列出最近的n条命令 

pwd（英文全拼：print work directory）: 命令用于显示工作目录。执行 pwd 指令可立刻得知您目前所在的工作目录的绝对路径名称。



export 命令用于设置或显示环境变量。在 shell 中执行程序时，shell 会提供一组环境变量。export 可新增，修改或删除环境变量，供后续执行的程序使用。

```
export [-fnp][变量名称]=[变量设置值]

    -f 　代表[变量名称]中为函数名称。
    -n 　删除指定的变量。变量实际上并未删除，只是不会输出到后续指令的执行环境中。
    -p 　列出所有的shell赋予程序的环境变量。

```
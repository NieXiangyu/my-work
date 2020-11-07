1.ssh的使用：https://blog.csdn.net/li528405176/article/details/82810342

Secure Shell(SSH) 是由 IETF(The Internet Engineering Task Force) 制定的建立在应用层基础上的安全网络协议。它是专为远程登录会话(甚至可以用Windows远程登录Linux服务器进行文件互传)和其他网络服务提供安全性的协议，可有效弥补网络中的漏洞。通过SSH，可以把所有传输的数据进行加密，也能够防止DNS欺骗和IP欺骗。还有一个额外的好处就是传输的数据是经过压缩的，所以可以加快传输的速度。目前已经成为Linux系统的标准配置。SSH只是一种协议，存在多种实现，既有商业实现，也有开源实现。

2.Argparse 介绍：（main.py中出现）：https://docs.python.org/zh-cn/3/howto/argparse.html

 Python 内置的一个用于命令项选项与参数解析的模块，通过在程序中定义好我们需要的参数，argparse 将会从 sys.argv 中解析出这些参数，并自动生成帮助和使用信息。命令行操作启动时使用起作用解析命令行参数。

 ArgumentParser 对象:https://docs.python.org/zh-cn/3/library/argparse.html#

:创建一个新的 [`ArgumentParser`](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser) 对象。所有的参数都应当作为关键字参数传入。

add_argument() 方法:定义单个的命令行参数应当如何解析。

add_subparsers()方法:创建子命令（https://blog.csdn.net/qq_41629756/article/details/105689494）

set_defaults()方法:可以将子命令绑定特定的函数。

parse_args()：

```
parse_args(args=None, nampespace=None)
```

args - 参数名称，namespace - 赋值，对 add_argument() 中定义的参数进行赋值

其中：action 命名参数:指定了这个命令行参数应当如何处理。（https://yongqiang.blog.csdn.net/article/details/103782730）

3.if __name__ == "__main__":https://www.cnblogs.com/chenhuabin/p/10118199.html

4.Peewee:(__init__.py中使用):https://www.jianshu.com/p/8d1bdd7f4ff5
database = PostgresqlDatabase()建立数据库，然后database.create_tables()创建表。

其中，PostgreSQL 是一个免费的对象-关系数据库服务器(ORDBMS)，有关详细教程：https://www.runoob.com/postgresql/postgresql-tutorial.html

5.py2neo:(__init__.py中使用):https://blog.csdn.net/jian_qiao/article/details/100557985
用于连接图与数据库。创建、查询节点与图。

6.playhouse.reflection：https://www.osgeo.cn/peewee/peewee/interactive.html
playhouse.reflection.generate_models -从现有数据库生成模型。这个 generate_models() 函数将自省数据库并为找到的所有表生成模型类。函数返回一个由表名键控的字典，生成的模型作为相应的值。

7.roslib:（ros.py中使用）:
基本看到函数名就能知道作用。
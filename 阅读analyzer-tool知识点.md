# 1.ssh的使用：https://blog.csdn.net/li528405176/article/details/82810342

Secure Shell(SSH) 是由 IETF(The Internet Engineering Task Force) 制定的建立在应用层基础上的安全网络协议。它是专为远程登录会话(甚至可以用Windows远程登录Linux服务器进行文件互传)和其他网络服务提供安全性的协议，可有效弥补网络中的漏洞。通过SSH，可以把所有传输的数据进行加密，也能够防止DNS欺骗和IP欺骗。还有一个额外的好处就是传输的数据是经过压缩的，所以可以加快传输的速度。目前已经成为Linux系统的标准配置。SSH只是一种协议，存在多种实现，既有商业实现，也有开源实现。

# 2.Argparse 介绍:（main.py中出现）：https://docs.python.org/zh-cn/3/howto/argparse.html

 Python 内置的一个用于命令项选项与参数解析的模块，通过在程序中定义好我们需要的参数，argparse 将会从 sys.argv 中解析出这些参数，并自动生成帮助和使用信息。命令行操作启动时使用起作用解析命令行参数。

## ArgumentParser 对象:https://docs.python.org/zh-cn/3/library/argparse.html#

:创建一个新的 [`ArgumentParser`](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser) 对象。所有的参数都应当作为关键字参数传入。

*class* `argparse.ArgumentParser`(*prog=None*, *usage=None*, *description=None*, *epilog=None*, *parents=[]*, *formatter_class=argparse.HelpFormatter*, *prefix_chars='-'*, *fromfile_prefix_chars=None*, *argument_default=None*, *conflict_handler='error'*, *add_help=True*, *allow_abbrev=True*, *exit_on_error=True*)

参数[description](https://docs.python.org/zh-cn/3/library/argparse.html#description) : 在参数帮助文档之前显示的文本（默认值：无）

### add_argument() 方法:定义单个的命令行参数应当如何解析。形参作用如下：

第一个必要参数：[name or flags](https://docs.python.org/zh-cn/3/library/argparse.html#name-or-flags) - 一个命名或者一个选项字符串的列表

[action](https://docs.python.org/zh-cn/3/library/argparse.html#action) - 当参数在命令行中出现时使用的动作基本类型。大多数动作只是简单的向 parse_args()返回的对象上添加属性。

[dest](https://docs.python.org/zh-cn/3/library/argparse.html#dest) - 被添加到 [`parse_args()`](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser.parse_args) 所返回对象上的属性名。

[help](https://docs.python.org/zh-cn/3/library/argparse.html#help) - 一个此选项作用的简单描述。



### add_subparsers()方法:[创建子命令](https://blog.csdn.net/qq_41629756/article/details/105689494)

 [add_subparsers()](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser.add_subparsers) 方法通常不带参数地调用并返回一个特殊的动作对象。 这种对象只有一个方法 `add_parser()`，它接受一个命令名称和任意多个 [`ArgumentParser`](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser) 构造器参数，并返回一个可以通常方式进行修改的 [`ArgumentParser`](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser) 对象。



### set_defaults()方法:可以将子命令绑定特定的函数。

[parse_args()](https://docs.python.org/zh-cn/3/library/argparse.html#argparse.ArgumentParser.parse_args) 方法支持多种指定选项值的方式（如果它接受选项的话）。 

```
parse_args(args=None, nampespace=None)
将参数字符串转换为对象并将其设为命名空间的属性。 返回带有成员的命名空间。
```

args - 参数名称，namespace - 赋值，对 add_argument() 中定义的参数进行赋值







# 4.Peewee:(__init__.py中使用):https://www.jianshu.com/p/8d1bdd7f4ff5
database = PostgresqlDatabase()建立数据库，然后database.create_tables()创建表。

其中，PostgreSQL 是一个免费的对象-关系数据库服务器(ORDBMS)，有关详细教程：https://www.runoob.com/postgresql/postgresql-tutorial.html

先定义Model，然后通过`db.create_tables()`创建或`Model.create_table()`创建表。

Package等类继承Model，数据结构包括什么在这个类中定义

更详细教程：https://www.cnblogs.com/yxi-liu/p/8514763.html



ForeignKeyField：

backref = 'str' 设置反向引用的访问器名称，类似于Django中设置外键字段是配置的related_name。



Meta:

indexes 设置要索引的字段列表，可以设置联合索引，类似Django的联合索引设置。可以通过继承设置。



# 5.py2neo:(__init__.py中使用):用于连接图与数据库。创建、查询节点与图。py2neo对Neo4j图形数据库进行操作。

[Py2neo的基本用法](https://blog.csdn.net/jian_qiao/article/details/100557985)

[py2neo——Neo4j&python的配合使用](https://www.jianshu.com/p/a2497a33390f)



# 6.playhouse.reflection：https://www.osgeo.cn/peewee/peewee/interactive.html
playhouse.reflection.generate_models -从现有数据库生成模型。这个 generate_models() 函数将自省数据库并为找到的所有表生成模型类。函数返回一个由表名键控的字典，生成的模型作为相应的值。

# 7.roslib:（ros.py中使用）:
基本看到函数名就能知道作用。

# 8.psycopg2，是Python语言的PostgreSQL数据库接口

参考教程：https://www.cnblogs.com/yy3b2007com/p/5724427.html



# 9.import re:Python的re模块，是常用的正则表达式处理函数。

参考教程：https://blog.csdn.net/c20081052/article/details/80920073

sub() 方法提供一个替换值，可以是字符串或一个函数，和一个要被处理的字符串



# 10.import os:在自动化测试中，经常需要查找操作文件，比如说查找配置文件（从而读取配置文件的信息），查找测试报告（从而发送测试报告邮件），经常要对大量文件和大量路径进行操作，这就依赖于os模块

参考教程:https://www.cnblogs.com/yufeihlf/p/6179547.html

`os.path.relpath（*path* [，*start* ] ）

将相对*路径*从当前目录或可选的*开始*目录中返回到*路径*。这是一个路径计算：不访问文件系统来确认*路径*或 *启动*的存在或性质。



[os.environ](https://blog.csdn.net/qq_25680531/article/details/80922783)是一个字符串所对应环境的映像对象



os.path.join()函数：连接两个或更多的路径名组件

1.如果各组件名首字母不包含’/’，则函数会自动加上

2.如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃

3.如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾



# python:
## if __name__ == "__main__":https://www.cnblogs.com/chenhuabin/p/10118199.html

## from copy import deepcopy:

[deepcopy](https://blog.csdn.net/u010712012/article/details/79754132)

## *args
*和  **  运算符:https://blog.csdn.net/yilovexing/article/details/80577510

## join()
[join()](https://www.runoob.com/python/att-string-join.html])方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

## isinstance()
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。

 ## strip() 
用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

## @[函数装饰器](http://c.biancheng.net/view/2270.html)
使用函数装饰器 A() 去装饰另一个函数 B()，其底层执行了如下 2 步操作：
    将 B 作为参数传给 A() 函数；
    将 A() 函数执行完成的返回值反馈回  B。



# Launch:
 $(env ENVIRONMENT_VARIABLE)  由当前环境变量来代替参数值，如果没有设置当前变量，则会失败

$(optenv ENVIRONMENT_VARIABLE)   $(optenv ENVIRONMENT_VARIABLE default_value)   参数值为设置的环境变量，如果  default_value设置了就使用default_value为参数值


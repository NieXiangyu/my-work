from .edge import Edge
from .node import Node
from graphviz import Digraph
from Launchviz.exceptions import *


class Graph:
    # kind = ['node', 'launch', 'package']
    # 存储节点（从 1 开始）、边（从101开始）的种类信息
    # kind_type = {'node': 1, 'launch': 2, 'package': 3, 'include': 101}
    # 节点使用的宏定义
    KIND_NODE = 1
    KIND_LAUNCH = 2
    KIND_PACKAGE = 3
    node_kinds = [KIND_NODE, KIND_LAUNCH, KIND_PACKAGE]
    EDGE_INCLUDE = 101
    edge_kinds = [EDGE_INCLUDE]
    # 样式
    # 这些节点，边和图属性的详细含义见官网http://graphviz.org/doc/info/attrs.html
    style = [{'style': 'filled', 'color': 'deepskyblue', 'fillcolor': 'deepskyblue', 'fontcolor': 'white'},  # node
             {'style': 'rounded', 'shape': 'box'},  # launch
             {'color': 'orange', 'fontcolor': 'orange'}]  # package

    def __init__(self, name: str, filename: str = '', render_type: str = 'pdf', engine: str = 'dot'):
        '''
        初始化Graph对象
        @param name:图名
        @param filename:文件名
        @param render_type:图片输出格式（pdf,png等）
        @param engine:见官网Roadmap，（dot，neato,fdp,sfdp,circo等格式，dot为分层有向图，有向图默认使用）
        '''
        # 存储现有节点的名字
        self.node_name = []

        # 存储子图（用于确定节点类型对应的样式）
        self.__subgraph = []

        self.name = name
        #文件名没写默认使用name图名
        if filename == '':
            self.filename = name
        #文件名自己写了就用
        else:
            self.filename = filename   
        self.render_type = render_type  

        # 建立一个图
        #dot语法的关键字：
        #graph, 无向图. 在图的创建时必须声明为有向图还是无向图
        #digraph, 有向图
        #node, 节点
        #edge, 边
        #subgraph, 子图
        self.dot = Digraph(name=self.name, filename=self.filename, format=self.render_type, engine=engine)
        # 建立子图
        # 图形引擎（engine)也可以称之为“支持应用的底层函数库”或者说是对特定应用的一种抽象,
        self.node = Digraph('node')
        self.dot.subgraph(self.node)
        self.__subgraph.append(self.node)
        # TODO：下一版本建立字典分析处理函数
        # self.node.attr('node', style='filled')
        #KIND_NODE = 1
        #style = [{'style': 'filled', 'color': 'deepskyblue', 'fillcolor': 'deepskyblue', 'fontcolor': 'white'},  # node
        #     {'style': 'rounded', 'shape': 'box'},  # launch
        #    {'color': 'orange', 'fontcolor': 'orange'}]  # package
        self.node.attr('node', style=self.style[self.KIND_NODE - 1]['style'])
        self.node.attr('node', color=self.style[self.KIND_NODE - 1]['color'])
        self.node.attr('node', fillcolor=self.style[self.KIND_NODE - 1]['fillcolor'])
        self.node.attr('node', fontcolor=self.style[self.KIND_NODE - 1]['fontcolor'])
        
        #KIND_LAUNCH = 2
        self.launch = Digraph('launch')
        self.dot.subgraph(self.launch)
        self.__subgraph.append(self.launch)
        self.launch.attr('node', style=self.style[self.KIND_LAUNCH - 1]['style'])
        self.launch.attr('node', shape=self.style[self.KIND_LAUNCH - 1]['shape'])
        # self.launch.attr('node', style='diagonals')

        KIND_PACKAGE = 3
        self.package = Digraph('package')
        self.dot.subgraph(self.package)
        self.__subgraph.append(self.package)
        self.package.attr('node', color=self.style[self.KIND_PACKAGE - 1]['color'])
        self.package.attr('node', fontcolor=self.style[self.KIND_PACKAGE - 1]['fontcolor'])
        # 进行test

    def add_node(self, kind: int, name: str, label: str = ""):
        '''
        作用：增加结点
        @param kind:节点种类，输入1,2,3，含义见node_kinds[]
        @type kind:int
        @param name:节点名
        @type name:str
        @param label:节点标签，不输入默认为节点名
        @type label:str
        '''

        # 检查 name 是否符合要求
        # 当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。
        # 一旦执行了raise语句，raise后面的语句将不能执行。
        if name in self.node_name:
            ex = NodeDuplicationErr('The node ' + name + ' has already existed!')
            raise ex
        self.node_name.append(name)

        # 处理 label，无标签自动用name作为默认标签
        if label == "":
            label = name

        # 对 kind 输入进行检查
        # 之前定义node_kinds = [KIND_NODE, KIND_LAUNCH, KIND_PACKAGE]
        if kind not in self.node_kinds:
            ex = NodeKindErr('Cannot find NODE KIND: ' + str(kind))
            raise ex

        # 实例化一个 Node
        Node(name, label, subgraph=self.__subgraph[kind - 1])

        # 将通过子图建立的点添加到 dot 中
        self.dot.subgraph(self.__subgraph[kind - 1])

        # print(self.__subgraph)
        # print(type(self.__subgraph[kind - 1]))

    def add_edge(self, head: str, tail: str, kind: int = EDGE_INCLUDE):
        '''
        作用：增加边
        @param head:头结点名
        @type head:str
        @param tail:尾节点名
        @type tail:str
        @param kind:边类型，见宏定义edge_kinds[],暂时只有101
        @type kind:int
        '''
        # 对 head tail 进行检查
        if head not in self.node_name:
            ex = NodeNotFoundErr('\nThe HEAD node: ' + head +
                                 ' is not defined! You can use nodes() to get a list of nodes existed.',
                                 position=NodeNotFoundErr.POSITION_HEAD)
            raise ex
        elif tail not in self.node_name:
            ex = NodeNotFoundErr('\nThe TAIL node: ' + tail +
                                 ' is not defined! You can use nodes() to get a list of nodes existed.',
                                 position=NodeNotFoundErr.POSITION_TAIL)
            raise ex

        # 检查 kind
        if kind not in self.edge_kinds:
            ex = EdgeKindErr('Cannot find the EDGE KIND: ' + str(kind))
            raise ex

        Edge(head=head, tail=tail, kind=kind, graph=self.dot)

    def nodes(self, view: bool = True):
    '''
        作用：查看已有结点列表，抛出异常提示中出现此函数，提示使用此函数 
        @param  view: 输入true查看且打印结果，false仅仅得到返回值
        @type  view: bool
        @return: node.name: 返回现有节点名字的列表
        @rtype: list
    '''
        if view:
            print('Existing nodes: ', self.node_name)
        return self.node_name
    

    def render(self, view: bool = False):
        '''
            @param view:true则调用view(),save the source to file, open the rendered result in a viewer
                        false则调用render(),save the source to file and render with the Graphviz engine
            @type view :bool
        '''

        # 添加每加一个节点需要添加一次子图，故此处不需要再次子图
        # self.dot.subgraph(self.node)
        # self.dot.subgraph(self.launch)
        # self.dot.subgraph(self.package)
        if view:
            self.dot.view()
        else:
            self.dot.render()
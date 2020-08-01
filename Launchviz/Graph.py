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
    style = [{'style': 'filled', 'color': 'deepskyblue', 'fillcolor': 'deepskyblue', 'fontcolor': 'white'},  # node
             {'style': 'rounded', 'shape': 'box'},  # launch
             {'color': 'orange', 'fontcolor': 'orange'}]  # package

    def __init__(self, name: str, filename: str = '', render_type: str = 'pdf', engine: str = 'dot'):
        # 存储现有节点的名字
        self.node_name = []

        # 存储子图（用于确定节点类型对应的样式）
        self.__subgraph = []

        self.name = name
        if filename == '':
            self.filename = name
        else:
            self.filename = filename
        self.render_type = render_type

        # 建立一个图
        self.dot = Digraph(name=self.name, filename=self.filename, format=self.render_type, engine=engine)
        # 建立子图
        self.node = Digraph('node')
        self.dot.subgraph(self.node)
        self.__subgraph.append(self.node)
        # TODO：下一版本建立字典分析处理函数
        # self.node.attr('node', style='filled')
        self.node.attr('node', style=self.style[self.KIND_NODE - 1]['style'])
        self.node.attr('node', color=self.style[self.KIND_NODE - 1]['color'])
        self.node.attr('node', fillcolor=self.style[self.KIND_NODE - 1]['fillcolor'])
        self.node.attr('node', fontcolor=self.style[self.KIND_NODE - 1]['fontcolor'])

        self.launch = Digraph('launch')
        self.dot.subgraph(self.launch)
        self.__subgraph.append(self.launch)
        self.launch.attr('node', style=self.style[self.KIND_LAUNCH - 1]['style'])
        self.launch.attr('node', shape=self.style[self.KIND_LAUNCH - 1]['shape'])
        # self.launch.attr('node', style='diagonals')

        self.package = Digraph('package')
        self.dot.subgraph(self.package)
        self.__subgraph.append(self.package)
        self.package.attr('node', color=self.style[self.KIND_PACKAGE - 1]['color'])
        self.package.attr('node', fontcolor=self.style[self.KIND_PACKAGE - 1]['fontcolor'])
        # 进行test

    def add_node(self, kind: int, name: str, label: str = ""):
        # 检查 name 是否符合要求
        if name in self.node_name:
            ex = NodeDuplicationErr('The node ' + name + ' has already existed!')
            raise ex
        self.node_name.append(name)

        # 处理 label
        if label == "":
            label = name

        # 对 kind 输入进行检查
        if kind not in self.node_kinds:
            ex = NodeKindErr('Cannot find NODE KIND: ' + str(kind))
            raise ex

        # 实例化一个 node
        Node(name, label, subgraph=self.__subgraph[kind - 1])

        # 将通过子图建立的点添加到 dot 中
        self.dot.subgraph(self.__subgraph[kind - 1])

        # print(self.__subgraph)
        # print(type(self.__subgraph[kind - 1]))

    def add_edge(self, head: str, tail: str, kind: int = EDGE_INCLUDE):
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
        if view:
            print('Existing nodes: ', self.node_name)
        return self.node_name

    def render(self, view: bool = False):
        # 添加每加一个节点需要添加一次子图，故此处不需要再次子图
        # self.dot.subgraph(self.node)
        # self.dot.subgraph(self.launch)
        # self.dot.subgraph(self.package)
        if view:
            self.dot.view()
        else:
            self.dot.render()

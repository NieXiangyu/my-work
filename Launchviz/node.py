from graphviz import Digraph


class Node:
    # 若不使用子图的方式设定样式，则在此存储样式相关设置
    def __init__(self, name: str, label: str, subgraph: Digraph):
        subgraph.node(name=name, label=label)
        print('add node: ' + name)

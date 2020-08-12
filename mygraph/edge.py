from graphviz import Digraph


class Edge:
    def __init__(self, head: str, tail: str, kind: int, graph: Digraph):
        # 如有对 kind 的处理，则在此处添加
        # TODO: 下一版时在此加入样式文件读取功能
        if kind == 101:
            graph.edge(tail_name=head, head_name=tail)
            print('add edge: ', head, ' -> ', tail)
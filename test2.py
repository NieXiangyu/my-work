from Launchviz.Graph import Graph

g = Graph('test2', 'second graph')
g.add_node(g.KIND_NODE, 'node-1', 'func-1')
g.add_node(g.KIND_NODE, 'node-2')
g.add_node(g.KIND_NODE, 'node-3', 'func-3')
g.add_node(g.KIND_LAUNCH, 'func-1')
g.add_node(g.KIND_LAUNCH, 'func-2')
g.add_node(g.KIND_LAUNCH, 'func-3', 'func-1')
g.add_node(g.KIND_PACKAGE, 'ROOT')
g.add_node(g.KIND_PACKAGE, 'PKG-A')
g.add_node(g.KIND_PACKAGE, 'PKG-B')
g.add_node(g.KIND_PACKAGE, 'PKG-C')
g.add_node(g.KIND_PACKAGE, 'PKG-D', 'PKG-B')
g.nodes()
g.add_edge('ROOT', 'PKG-A')
g.add_edge('ROOT', 'PKG-B')
g.add_edge('PKG-A', 'PKG-C')
g.add_edge('PKG-A', 'PKG-D')
g.add_edge('PKG-B', 'PKG-C')
g.add_edge('PKG-B', 'func-1')
g.add_edge('PKG-C', 'func-2')
g.add_edge('PKG-D', 'func-3')
g.add_edge('func-3', 'node-3')
g.add_edge('func-1', 'node-1')
g.add_edge('func-2', 'node-2')
g.render()



g.render(True)

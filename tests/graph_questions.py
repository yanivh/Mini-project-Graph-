from models import graph ,node


def creatgraphs():
    nodes = []
    mnode = node.Node('1', {})
    mnode.add_edge('5', 20)
    mnode.add_edge('6', 5)
    mnode.add_edge('7', 15)
    mnode.add_edge('2', 10)
    mnode.add_edge('4', 20)

    nodes.append(mnode)

    mnode = node.Node('2', {})
    mnode.add_edge('4', 10)
    mnode.add_edge('3', 20)

    nodes.append(mnode)

    mnode = node.Node('3', {})
    mnode.add_edge('4', 5)
    mnode.add_edge('2', 15)

    nodes.append(mnode)

    mnode = node.Node('4', {})
    mnode.add_edge('5', 10)

    nodes.append(mnode)
    graph1 = graph.Graph('1',nodes)


    nodes = []
    mnode = node.Node('5', {})
    mnode.add_edge('6', 5)

    nodes.append(mnode)

    mnode = node.Node('6', {})
    nodes.append(mnode)

    mnode = node.Node('7', {})
    mnode.add_edge('6', 10)
    nodes.append(mnode)

    graph2 = graph.Graph('2',nodes)


    nodes = []
    mnode = node.Node('8', {})
    mnode.add_edge('1', 5)
    mnode.add_edge('2', 20)
    mnode.add_edge('7', 5)
    nodes.append(mnode)

    mnode = node.Node('9', {})
    mnode.add_edge('8', 20)
    mnode.add_edge('2', 15)
    mnode.add_edge('10', 10)
    nodes.append(mnode)

    mnode = node.Node('10', {})
    mnode.add_edge('2', 5)
    mnode.add_edge('3', 15)
    nodes.append(mnode)

    graph3 = graph.Graph('3',nodes)
    return graph1,graph2,graph3


# Question 1
# Create 3 Graph objects, each contains a different collection of nodes, which together contain all 10 nodes.
# Use the __add()__ method to create a total graph that contains the entire data of the example.
graph1,graph2,graph3=creatgraphs()
graph_1_2 =graph1+graph2
graph_1_2_3 = graph_1_2+graph3

graph1.printnodes()
graph2.printnodes()
graph3.printnodes()

graph_1_2.printnodes()
graph_1_2_3.printnodes()

# Question 3
# Sort the nodes by the number of their reachable nodes.

# Question 4
# What is the pair of nodes that the shortest path between them has the highest weight?





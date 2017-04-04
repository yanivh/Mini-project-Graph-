from models import graph ,node

#node 10
def CreateexistNodewithnewedge():

    # init - empty node
    mnode = node.Node('10', {})
    mnode.add_edge('12', 20)
    mnode.add_edge('15', 20)
    return mnode

# Node 11
def CreateNodes2():
    nodes = []
    mnode = node.Node('11', {})
    mnode.add_edge('11', 20)
    mnode.add_edge('12', 15)
    mnode.add_edge('13', 10)
    nodes.append(mnode)

    return nodes

#nodes : 1-10
def CreateNodes():
    nodes = []

    # init - empty node
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

    mnode = node.Node('5', {})
    mnode.add_edge('6', 5)

    nodes.append(mnode)

    mnode = node.Node('6', {})
    nodes.append(mnode)

    mnode = node.Node('7', {})
    mnode.add_edge('6', 10)
    nodes.append(mnode)

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

    return nodes

#init
nodes =CreateNodes()
mygraph1 = graph.Graph('x',nodes)


existnode= CreateexistNodewithnewedge()
mygraph1.add_node(existnode)

nodes2 =CreateNodes2()
mygraph2 = graph.Graph('Y',nodes2)


# Magic functions:
print('\n__str__  - print (mygraph1)' )
print (mygraph1)

print ('\n__len__ - nodes number :{}\n'.format(len(mygraph1)))

print ('\n__add__ - new_graph = Y+X :'.format())
new_graph = mygraph1+mygraph2

#include nodes: 1-11
print(new_graph)



print ('\n mygraph1.is_reachable(6,1) = {}'.format(mygraph1.is_reachable('6','1')))
print ('\n mygraph1.is_reachable(7,6) = {}'.format(mygraph1.is_reachable('7','6')))

print ('\n mygraph1.find_all_paths(6,1) :\n'.format())
paths= mygraph1.find_all_paths('1','6')
for p in paths:
  print (p)

print ('\n mygraph1.get_edge_weight(1,5) : {}'.format(mygraph1.get_edge_weight('1','5')))


path=[8,1,5,6]
print('path=[8,1,5,6] - get_path_weight : {}'.format(mygraph1.get_path_weight(path)))


#add exist node with new edge
print('\nadd exist node with new edge :\n')
existnode= CreateexistNodewithnewedge()
mygraph1.add_node(existnode)

print ('new_graph.remove_node(9)')
new_graph.remove_node('9')
print (new_graph)


print ('new_graph.remove_node(1,10,9)')
new_graph.add_edge('1','10',10)
print(new_graph)

print('new_graph.is_edge(1,10) : {}'.format(new_graph.is_edge('1','10')))

print('new_graph.is_reachable(4,5) : {}'.format(new_graph.is_reachable('4','5')))


from models import graph ,node, nondirectionalgraph


# init - empty node graph
mygraph1 = nondirectionalgraph.NonDirectionalGraph('x',{})


mynode= node.Node('1',{})
mygraph1.add_node(mynode)

mynode= node.Node('2',{})
mygraph1.add_node(mynode)

mygraph1.addedge('1','2')


print(mygraph1)



from models import node, graph

# init - empty node
mynode= node.Node('A',{})

print ('\n Node name is {}' .format(mynode.name))

#check is isolated
if mynode.is_isolated():
    print('\n mynode.is_isolated()- result : Node is empty')
else:
    print('\n length of Node {}= {}'.format(mynode.name,len(mynode)))

#fill with information
mynode.add_edge('1',5)
mynode.add_edge('2',10)
mynode.add_edge('3',15)

print('\n mynode.add_edge(1,5) \n mynode.add_edge(2,10) \n mynode.add_edge(3,15) \n after filling with information :length of Node {} = {} \n'.format(mynode.name,len(mynode)))


#Add edge with simlar name to exist edge
print ('\n mynode.add_edge(1,5) , result:')
mynode.add_edge('1',5)

#Add edge with simlar name to node name
print ('\n add edge with name silimar to node: \n mynode.add_edge(A,5) , result:')
mynode.add_edge('A',5)

#remove edge
print ('\n Remove edge : \n mynode.remove_edge(1) , result:')
mynode.remove_edge('1')


#remove edge not exist
print('\n remove non exist Edge {}  from {} result:'.format('1',mynode.name,len(mynode)))
mynode.remove_edge('1')

#get weight of specific edge
print ('\n node 2 weight is {}'.format(mynode.get_weight('2')))

#Check if edge is part of Node
print ('\n is edge 2 in {} = {}'.format(mynode.name,mynode.is_edge('2')))

#__eq__ & _ne_ magic function
nodeA= node.Node('A',{})
nodeB= node.Node('A',{})
nodeC= node.Node('C',{})

print ('\n\n __eq__ & _ne_ magic function: ')
print('\nnodeA= node.Node(A,{})\nnodeB= node.Node(A,{}) \nnodeC= node.Node(C,{})')

print('\nnodeA==nodeB : {}'.format(nodeA==nodeB))
print('nodeA==nodeC : {}'.format(nodeA==nodeC))

print('nodeA!=nodeB : {}'.format(nodeA!=nodeB))
print('nodeA!=nodeC : {}'.format(nodeA!=nodeC))
from models import node, graph
import functools as ft

# Question 1 + 2
# Create 10 Node objects according to the figure above
def CreateNodes():

        nodes=[]

        # init - empty node
        mnode= node.Node('1',{})
        mnode.add_edge('5',20)
        mnode.add_edge('6',5)
        mnode.add_edge('7',15)
        mnode.add_edge('2',10)
        mnode.add_edge('4',20)

        nodes.append(mnode)

        mnode= node.Node('2',{})
        mnode.add_edge('4',10)
        mnode.add_edge('3',20)

        nodes.append(mnode)

        mnode= node.Node('3',{})
        mnode.add_edge('4',5)

        nodes.append(mnode)

        mnode= node.Node('4',{})
        mnode.add_edge('5',10)

        nodes.append(mnode)

        mnode= node.Node('5',{})
        mnode.add_edge('6',5)

        nodes.append(mnode)

        mnode= node.Node('6',{})
        nodes.append(mnode)

        mnode= node.Node('7',{})
        mnode.add_edge('6',10)
        nodes.append(mnode)

        mnode= node.Node('8',{})
        mnode.add_edge('1',5)
        mnode.add_edge('2',20)
        mnode.add_edge('7',5)
        nodes.append(mnode)

        mnode= node.Node('9',{})
        mnode.add_edge('8',20)
        mnode.add_edge('2',15)
        mnode.add_edge('10',10)
        nodes.append(mnode)


        mnode= node.Node('10',{})
        mnode.add_edge('2',5)
        mnode.add_edge('3',15)
        nodes.append(mnode)

        return nodes

def printnodes(nodes):
    for n in nodes:
        print('\n Node{}, contains {} edges'.format(n.name, len(n)))
        for k,v in n.edges.items():
            print ('  Key:{}, value:{}'.format(k,v))

def countedges(nodes):
    count=0
    for n in nodes:
        for e in n.edges.keys():
            count= count +1
    return count

# Question 3
# How many edges are in the graph, and what is their total weight?
def calculateweight(nodes):
    totalweight=0
    for n in nodes:
        if len(n.edges)>0:
            weight= (ft.reduce(lambda x, y: x + y, n.edges.values()))
            totalweight= totalweight+ weight
    return totalweight

nodes= CreateNodes()
printnodes(nodes)

print ('\ntotal numbers of edges are :{}'.format(countedges(nodes)))
print ('\ntotal edges weight is :{}'.format(calculateweight(nodes)))

# Question 4
# Sort the nodes by the number of their edges : big the small

print('\nSort the nodes by the number of their neighbors :')
for k in sorted(nodes, key=lambda k: len(k.edges), reverse=True):
    print('node: {}, contain : {} '.format(k,len(k.edges)))





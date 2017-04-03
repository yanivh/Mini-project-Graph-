from models import graph ,node, nondirectionalgraph
from random import randint

# init - empty node graph
mygraph1 = nondirectionalgraph.NonDirectionalGraph('social',{})

def proccessdata(name):

    #print (name)
    #parmeters
    i = 1
    nodesdict = {}
    countdict ={}
    #print(len(paths))

    namesdict={}
    connections=[]
    with open(name) as f:
        for line in f:

         connection = line.split(' ')
         connections.append(connection)
         #Fill unique names dictionary
         namesdict[line.split(' ')[0]] = randint(0, 100)

    return connections , namesdict

soical , namesdict=proccessdata('social.txt')


#Create Nodes
for k,v in namesdict.items():
    #print (k,v)
    _node = node.Node(k,{})
    mygraph1.add_node(_node)

#add or remove edges between nodes
for line in soical:

    if line[3] == 'became':
        mygraph1.addedge(line[0], line[2])

    elif line[3] == 'cancelled':
        mygraph1.removeedge(line[0], line[2])

print(mygraph1)

#check id path exit
print ( mygraph1.is_edge('Gad','Judah'))

#find short way between friends
paths=mygraph1.find_shortest_path('Gad','Simeon')
for path in paths:
   print(path)
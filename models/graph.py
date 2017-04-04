import functools as ft
import itertools as it
from models import node

class Graph :

    def __init__(self,name,nodes=[]):
        self.name=name
        self.nodes = {}
        for _node in nodes:
            self.add_node(_node)
            #for node in nodes:
            #    if node not in self.nodes:
            #        nodekey=node.name
            #        nodevalues=node.edges
            #        self.nodes[nodekey]= nodevalues

    #concat 2 graphs
    def __add__(self,other_graph):

        #create empty graph , name = concat garph1+ graph2
        new_graph = Graph('{}_{}'.format(other_graph.name,self.name),[])

        # add local graph nodes to new graph
        for k,v in self.nodes.items():
            new_graph.nodes[str(k)]=v

        #add other graph nodes to new graph
        for k,v in other_graph.nodes.items():
            new_graph.nodes[str(k)]=v

        return new_graph

    def __str__(self):
        return(self.printnodes())

    #def __getitem_(self,name):
    #    for k, v in self.nodes.items():
    #       if k==name:
    #            self.nodes[k]
    #        else:
    #            raise KeyError

    def __len__(self):
        count=0
        for x in self.nodes:
         count= count+1
        return count

    def printnodes(self):

        print('\n\n graph  {} , content  :'.format(self.name))

        content=''

        for k,v in self.nodes.items():
            content=content+ ('\nNode {}, contains {} edges'.format(k, len(v)))
            for vk,vv in self.nodes[k].edges.items():
                content=content+('\nKey:{}, value:{}'.format(vk , vv))
            content = content + '\n'
        return content

    def add_node(self,_node):

        is_node_exist = False
        #check if a node with the same name already exists in the graph
        # then existing edges should not be overwritten, but new edges should be added
        for kk,vv in self.nodes.items():
            if kk == _node.name:
               is_node_exist=True
               #found item
               for k,v in _node.edges.items():
                   self.nodes[kk].add_edge(k,v)

        #No Node Found then add to Graph
        if is_node_exist== False:
            #cast to Node Model
            newnode= node.Node(_node.name,{})
            if len(_node.edges.items())>0:
                for k,v in _node.edges.items():
                    newnode.add_edge(k,v)
                    self.nodes[_node.name]=newnode
            else:
                self.nodes[_node.name] = newnode

    def remove_node(self, name):
        key_to_remove = ''
        for k in self.nodes.keys():
            if k == name:
                key_to_remove = k

        if key_to_remove != '':
            self.nodes.pop(key_to_remove)
            print(' {} Removed successfully from Node {}'.format(key_to_remove, self.name))
        elif key_to_remove == '':
            print(' {} is not found'.format(name))

    # adds an edge making to_name a neighbor of frm_name.
    def add_edge(self, frm_name, to_name, weight=1):
        for k in self.nodes.keys():
            #if k.name == frm_name:
            if k == frm_name:
                self.nodes[k].edges[to_name] = weight

    # adds an edge making to_name a neighbor of frm_name.*
    def remove_edge(self, frm_name, to_name):
        key_to_remove=''
        for k in self.nodes.keys():
            #if k.name == frm_name:
            if k == frm_name:
                key_to_remove=k
                self.nodes[k].edges.pop(to_name)

    # returns True if to_name is a neighbor of frm_name
    def is_edge(self, frm_name, to_name):
        for k in self.nodes.keys():
            if k == frm_name:
                if to_name in self.nodes[k].edges.keys():
                    return True
                else:
                    return False

    # returns True if to_name is reachable from frm_name
    def is_reachable(self, frm_name, to_name):

        path=[]
        if len(self.find_all_paths(frm_name,to_name,path))>0:
            return True
        else:
            return False
    
    # Recursive  - mapping all paths from frm_name to to_name
    def find_all_paths(self, frm_name, to_name, path=[]):
        path = path + [frm_name]
        if frm_name == to_name:
            return [path]
        if frm_name not in self.nodes:
            return []

        paths = []

        if len(self.nodes[frm_name])>0:
            for node in self.nodes[frm_name].edges:
                x=len(self.nodes[frm_name])
                #print('self.nodes[frm_name]={} ,\n items {} \n,len :{}'.format(frm_name,self.nodes[frm_name],x))
                #print (node)
                if node not in path:
                #    print('{} not in {}'.format(node, path))
                    newpaths = self.find_all_paths( node, to_name,path)
                    #print ('newpaths : {}'.format(newpaths))
                    for newpath in newpaths:
                        paths.append(newpath)
        return paths

    #find the short path = less edges
    def find_shortest_path(self, frm_name, to_name):
        allpaths= []
        allpaths= self.find_all_paths(frm_name,to_name)

        paths=[]
        items=[]
        shortpaths=[]

        for _item in allpaths:
            #({k:v})
            paths.append(len(_item))

        #Get min value
        minvalue= str(min(paths))


        for _item in allpaths:
            if str(len(_item))== minvalue:
                shortpaths.append(_item)

        return shortpaths

    # get edge weight - return none
    def get_edge_weight(self,frm_name,to_name):
        for node in self.nodes:
            if node == frm_name:
                for ek,ev in self.nodes[node].edges.items():
                    if ek==to_name:
                        return ev

    #calculate weight of give path- usually list of nodes
    def get_path_weight(self, path):

        length = len (path)
        i=0
        sedge=0
        stotal=0

        while length>=i:
            sedge=self.get_edge_weight(str(path[i]), str(path[i+1]))
            stotal= stotal+sedge

            i = i + 1
            length = length - 1

        else:
            return stotal


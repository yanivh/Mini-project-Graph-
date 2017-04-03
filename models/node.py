import functools as ft

class Node:
    def __init__(self, name, edges):
        self.name = name
        self.edges = {}
        if len(edges)>0:
            for e in edges:
                self.add_edge(str(e),edges[e])


    def __str__(self):
        return self.name

    # Count number of edges (neighbors)
    def __len__(self):
        count = 0
        for i in self.edges:
         count = count+1
        return count

    def __eq__(self, other): #triggered on objects ==
        if self.name != other:
           return False
        elif self.name== other:
            return True

    def __ne__(self, other): #triggered on objects !=
        if self.name == other:
           return False
        elif self.name!= other:
            return True

    def is_neighbor(self,name):
        for edge in self.edges:
            if edge==name:
                return True
            else:
                return False

    #Is Edge part of node
    def is_edge(self,name):
        is_edge = False
        for k in self.edges.keys():
             if k == name:
                 is_edge= True

        if is_edge :
          return  True

    # Add Edge
    def add_edge(self,name,weight=1):
        # not allow adding a edge with the same name as self.
        if name == self.name:
            print(' Node name & Edge name are similar , try different names')

        # not allow adding a edge with a name of an existing edge
        name_exist = False
        for k in self.edges.keys():
            if k == name:
                name_exist = True
                break

        if name_exist:
            print(' Edge already Exist , no Edge added')
        else:
            self.edges[name] = weight

    # Remove Edge
    def remove_edge(self,name):
        key_to_remove = ''
        for k in self.edges.keys():
             if k == name:
                 key_to_remove = k

        if key_to_remove != '' :
          self.edges.pop(key_to_remove)
          print(' {} Removed successfully from Node {}'.format(key_to_remove ,self.name))
        elif key_to_remove == '':
            print(' {} is not found'.format(name))

    # Get Weight
    def get_weight(self,name):
        weight=0
        for k in self.edges.keys():
             if k == name:
                  weight= self.edges[k]
        if weight==0:
            print(' {} is not part of {}'.format(name,self.name))
        else:
            return weight

    #check if Node if empty
    def is_isolated(self):
        count =0
        for k in self.edges.keys():
            count= count+1

        if count == 0:
            return True

# Make a dictionary of all prices over 200
#+p1 = { key:value for key, value in prices.items() if value > 200 }
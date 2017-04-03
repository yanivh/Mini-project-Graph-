from models import graph

class NonDirectionalGraph (graph.Graph):
    def __int__(self , name, nodes):
        graph.Graph.__init__(self,name,nodes)

    def addedge(self, frm_name, to_name, weight=1):
       self.add_edge(frm_name,to_name,weight=1)
       self.add_edge(to_name, frm_name, weight=1)


    def removeedge(self, frm_name, to_name, weight=1):
        self.remove_edge(frm_name,to_name)
        self.remove_edge( to_name,frm_name)
class Graph:
    def __init__(self):
        self.adj_dict = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.adj_dict.keys():
            self.adj_dict[vertex] = []
            
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_dict.keys() and v2 in self.adj_dict.keys():
            self.adj_dict[v1].append(v2)
            self.adj_dict[v2].append(v1)
            
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_dict.keys():
            for related_vertex in self.adj_dict[vertex]:
                self.adj_dict[related_vertex].remove(vertex)
                
            del self.adj_dict[vertex]
            
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_dict.keys() and v2 in self.adj_dict.keys():
            try:
                self.adj_dict[v1].remove(v2)
                self.adj_dict[v2].remove(v1)
            except ValueError:
                pass
            
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adj_dict:
            print(vertex, "->", self.adj_dict[vertex])
            

my_graph = Graph()
my_graph.add_vertex("IST")
my_graph.add_vertex("AMS")
my_graph.add_vertex("CDG")
my_graph.add_vertex("JFK")

my_graph.add_edge("IST", "AMS")
my_graph.add_edge("IST", "CDG")
my_graph.add_edge("IST", "JFK")
my_graph.add_edge("AMS", "CDG")
my_graph.add_edge("AMS", "JFK")
my_graph.add_edge("CDG", "JFK")

my_graph.print_graph()

print("---")

my_graph.remove_edge("AMS", "CDG")
my_graph.print_graph()


print("---")

my_graph.remove_vertex("JFK")
my_graph.print_graph()
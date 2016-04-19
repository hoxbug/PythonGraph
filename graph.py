class Graph:
    def __init__(self, graph_string):
        """Parses the graph string and sets the following attributes."""
        self.directed = None
        self.weighted = None
        self.adjacency_list = []

        graph_string = graph_string.strip().splitlines()
        header = graph_string.pop(0).split()

        if header[0] == "D":
            self.directed = True
        else:
            self.directed = False
        if len(header) == 3:
            self.weighted = True
            for i in range(1,int(header[2])):
                self.adjacency_list.append([])
        else:
            for i in range(0,int(header[1])):
                self.adjacency_list.append([])

        for edge in graph_string:
            edge = edge.split()
            edge = [ int(x) for x in edge ]
            if self.weighted:
                self.adjacency_list[edge[0]].append((edge[1],edge[2]))
                if not self.directed:
                    self.adjacency_list[edge[1]].append((edge[0],edge[2]))
            else:
                self.adjacency_list[edge[0]].append((edge[1],self.weighted))
                if not self.directed:
                    self.adjacency_list[edge[1]].append((edge[0],self.weighted))

    def print_graph(self):
        for vertex in self.adjacency_list:
            if vertex != []:
                vertex_num = self.adjacency_list.index(vertex)
                print("Vertex {0} adjacency list: {1}".format(vertex_num, vertex))

def process-edge(x,y):
    return_string = "Processed edge {} -> {}".format(x,y)
    return return_string

def process_vertex_early(v):
    return_string = "Processed vertex, {}, early".format(v)

def process_vertex_late(v):
    return_string = "Processed vertex, {}, late".format(v)

def bfs_tree(graph, start):
    """Returns the parents of each vertex, in the graph using a bfs search.
    The vertex without a parent is the root of the tree"""

    parents = [None for x in range(len(graph.adjacency_list))]
    processed = [False for x in range(len(graph.adjacency_list))]
    discovered = [False for x in range(len(graph.adjacency_list))]

    Queue = [start]

    while len(Queue) != 0:
        for edge in graph.adjacency_list[Queue[0]]:
            vertex, weight = edge
            if not discovered[vertex]:
                Queue.append(vertex)

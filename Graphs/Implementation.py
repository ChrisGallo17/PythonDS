class Graph: # Adjacency List

    def __init__(self):
        # self.nodes = set()  # all the vertexes in the graph using edges
        self.connections = {} # all the connections start_vertex:{end_vertex, weight}

    # def add_node(self, node):
        # self.nodes.add(node)
        
    def contains(self, v):
        return v in self.connections.keys()
    
    def connect(self, start, end, weight=1):
        # v = self.get_vertex(srt(from_vertex)) or Vertex(str(from_vertex))
        if start not in self.connections:
            self.connections[start] = {end:weight}
        else: self.connections[start][end] = weight

        if end not in self.connections:
            self.connections[end] = {}

    def get_nodes(self)


# Adjacency List object should have:
    # Graph() which creates an empty class
    # addVertex(vert) adds an instance of Vertex to graph
    # addEdge(fromVert, toVert) adds new directed edge that connects 2 verts
    # addEdge(fromVert, toVert, weight) same but with weight
    # getVertex(vertKey) finds vertex in graph named vertKey
    # getVerticies() returns a list of all vertecies in the graph 

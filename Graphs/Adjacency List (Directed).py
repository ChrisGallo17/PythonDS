# Vertex Class will represent each vertex in the graph
# This implementation uses directed edges
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {} # {nbr: weight}

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


# Graph class will hold the master list of vertices
class Graph: # Adjacency List
    def __init__(self):
        self.vertList = {} # {key: Vertex()}
        self.numVertices = 0

    def addVertex(self, key): # adds an instance of Vertex to graph
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
        
    def getVertex(self, n): # finds vertex in graph named n
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __contains__(self,n):
        return n in self.vertList

    def __iter__(self): 
        return iter(self.vertList.values())


    
g = Graph()

for i in range(6):
    g.addVertex(i)

print(g.vertList)


g.addEdge(0,1,2)

for vertex in g:
    print(vertex)
    print(vertex.getConnections())
    print('\n')
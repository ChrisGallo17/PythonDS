# Vertex Class will represent each vertex in the graph
# This implementation uses undirected edges
class Vertex():
    def __init__(self, key):
        self.id = key 
        self.connectedTo = {} #{nbr:weight}

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getweight(self, nbr):
        return self.connectedto[nbr]

# Graph class will hold the master list of vertices
class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVert = 0
    
    def addVertex(self, key):
        self.numVert += 1
        newVert = Vertex(key)
        self.vertList[key] = newVert
        return newVert

    def addEdge(self, f, t, weight = 0):
        if f not in self.vertList:
            nv = self.addVertex[f]
        if t not in self.vertList:
            nv = self.addVertex[t]
        self.vertList[f].addNeighbor(self.vertList[t], weight)
        self.vertList[t].addNeighbor(self.vertList[f], weight)

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def getVertices(self):
        return self.vertList.keys()

    def __contains__(self, n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())
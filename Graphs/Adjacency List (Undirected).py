class Vertex():
    def __init__(self, key):
        self.id = key 
        self.connectedTo = {} #{nbr:weight}

    def addNeighbor(self, nbr, weight):
        
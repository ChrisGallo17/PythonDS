# This graph implementation will use nodes and status states
# This graph has weighted edges and is directed

from enum import Enum
from collections import OrderedDict

class State(Enum):
    unvisited = 1 # White
    visited = 2   # Black
    visiting = 3  # Grey

class Node:
    def __init__(self, num):
        self.num = num
        self.visited_state = State.unvisited
        self.adjacent = OrderedDict() # key = node, val = node

    def __str__(self):
        return str(self.num)

class Graph:
    def __init__(self):
        self.nodes = OrderedDict() # key = node id, val = node

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, dest, weight = 0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight

g = Graph()

g.add_edge(0,1,3)

print(g.nodes)
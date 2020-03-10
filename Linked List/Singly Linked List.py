class Node(object):
    def __init__(self, data = None, next = None):
        self.value = data
        self.next = None

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node

class SinglyLinkedList(object):
    def __init__(self, head = None):
        self.head = None

    def insert(self, x):
        newNode = Node(x)
        newNode.set_next(self.head)
        self.head = newNode

    def remove(self, x):
        cur = self.head
        found = False
        #while 

    def size(self):
        cur = self.head
        count = 0
        while cur:
            cur = cur.get_next()
            count += 1
        return count

    def search(self, x):
        cur = self.head
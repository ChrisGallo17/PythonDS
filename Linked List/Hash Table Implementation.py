# Create a hash table that uses seperate chaining
# Each bucket will contain a linked list of nodes containing the objects stored at index
# This is for collision resolution

class HashTable:
    def __init__(self, INITIAL_CAPACITY):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        # for each character in the key
        for index, c in enumerate(key):
            # add(index + length of key)^(curent char code)
            hashsum += (index + len(key)) ** ord(c)
            # use modulus to keep hashsum in range [0, self.capacity - 1]
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        # if bucket is empty, create a node and add it 
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        # else: there is a collition, add it to the end of the list
        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        # now traverse the list at this node
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        # itterate the list
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
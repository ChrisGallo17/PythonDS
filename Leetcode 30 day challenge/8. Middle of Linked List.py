# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # traverse once to count the nodes
        # find the middle node
        # traverse until you get to the middle node and return it
        ref, count = head, 1
        while head.next != None:
            count += 1
            head = head.next
        count //= 2
        for x in range(count):
            ref = ref.next
        return ref
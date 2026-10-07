"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        og_to_new = {}

        curr = head
        while curr:
            og_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.random:
                og_to_new[curr].random = og_to_new[curr.random]
            if curr.next:
                og_to_new[curr].next = og_to_new[curr.next]
            curr = curr.next
        
        return og_to_new[head]


        
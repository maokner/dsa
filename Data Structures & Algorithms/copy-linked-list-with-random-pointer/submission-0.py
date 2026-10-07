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

        need_to_new = defaultdict(list)
        og_to_new = {}

        curr = head
        dummy = Node(67)
        prev = dummy

        while curr:
            new_curr = Node(curr.val)
            if curr.random == None:
                new_curr.random = None
            elif curr.random in og_to_new:
                new_curr.random = og_to_new[curr.random];
            else:
                need_to_new[curr.random].append(new_curr)
            prev.next = new_curr
            og_to_new[curr] = new_curr
            curr = curr.next

            prev = new_curr
        
        for need in need_to_new:
            for new in need_to_new[need]:
                new.random = og_to_new[need]        
        return dummy.next


        
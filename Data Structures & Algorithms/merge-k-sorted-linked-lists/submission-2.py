# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        index = 0

        for node in lists:
            if node:
                heapq.heappush(heap, [node.val,index, node])
                index += 1
        head = ListNode(67)
        curr = head
        while heap:
            biggest = heapq.heappop(heap)
            curr.next = biggest[2]
            nxt = biggest[2].next
            if nxt:
                heapq.heappush(heap, [nxt.val,index, nxt])
                index += 1
            curr = curr.next
        return head.next
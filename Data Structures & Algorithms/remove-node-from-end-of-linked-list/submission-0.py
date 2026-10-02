# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, fast = head, head
        l = 0
        while fast:
            fast = fast.next
            l += 1
        if l == n:
            return head.next
        numIter = l - n
        while numIter > 1:
            curr = curr.next
            numIter -= 1
        curr.next = curr.next.next
        return head
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry = 0
        while l1 and l2:
            newVal = l1.val + l2.val + carry
            curr.next = ListNode(newVal % 10)
            carry = newVal // 10
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            active = l1
        elif l2:
            active = l2
        else:
            active = None
        while active:
            newVal = carry + active.val
            curr.next = ListNode(newVal % 10)
            carry = newVal // 10
            curr = curr.next
            active = active.next
        if carry != 0:
            curr.next = ListNode(carry)
        return head.next




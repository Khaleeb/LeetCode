# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recur(self, l1, l2, prev, carry):
        if (l1 is None and l2 is None and carry is 0):
            return
        if l1 is not None:
            v1 = l1.val
            l1n = l1.next
        else:
            v1 = 0
            l1n = None
        if l2 is not None:
            v2 = l2.val
            l2n = l2.next
        else:
            v2 = 0
            l2n = None
        val = (v1 + v2 + carry) % 10
        carry = (v1 + v2 + carry) // 10
        cur = ListNode(val, None)
        prev.next = cur
        self.recur(l1n, l2n, cur, carry)
        return
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val = (l1.val + l2.val) % 10
        carry = (l1.val + l2.val) // 10
        head = ListNode(val, None)
        self.recur(l1.next, l2.next, head, carry)
        return head
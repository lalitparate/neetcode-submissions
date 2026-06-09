# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def add(self, l1, l2, carry):
        if not l1 and not l2 and carry == 0:
            return None
        
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        newVal = v1+v2+carry
        carry = newVal // 10
        val = newVal % 10

        l1Next = l1.next if l1 else None
        l2Next = l2.next if l2 else None
        next_node = self.add(l1Next, l2Next, carry)
        return ListNode(val, next_node)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1, l2, 0)

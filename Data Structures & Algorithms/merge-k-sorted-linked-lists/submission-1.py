# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) < 1:
            return None
        
        for i in range(1, len(lists)):
            lists[i] = self.merge(lists[i-1], lists[i])
        
        return lists[-1]
    
    def merge(self, l1, l2):
        dummy = ListNode()
        temp = dummy

        while(l1 and l2):
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        
        if l1:
            temp.next  = l1
        if l2:
            temp.next = l2
        return dummy.next
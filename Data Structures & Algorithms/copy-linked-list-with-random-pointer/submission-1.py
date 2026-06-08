"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None}

        cur = head
        while cur:
            if cur not in oldToCopy:
                oldToCopy[cur] = Node(cur.val)
            if cur.next not in oldToCopy:
                oldToCopy[cur.next] = Node(cur.next.val)
            oldToCopy[cur].next = oldToCopy[cur.next]
                
            if cur.random not in oldToCopy:
                oldToCopy[cur.random] = Node(cur.random.val)
            oldToCopy[cur].random = oldToCopy[cur.random]

            cur = cur.next
        
        return oldToCopy[head]

        
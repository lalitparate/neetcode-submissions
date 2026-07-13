"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        copy = Node(node.val)
        oldToNew[node] = copy

        q = deque()
        q.append(node)

        while(q):
            nd = q.popleft()
            for nei in nd.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[nd].neighbors.append(oldToNew[nei])
        return oldToNew[node]
                
        
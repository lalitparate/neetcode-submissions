# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.out = []
        q = deque([root])
        level = 0
        while(q):
            n = len(q)
            for i in range(n):
                ele = q.popleft()
                if ele:
                    if level == len(self.out):
                        self.out.append(ele.val)
                    
                    q.append(ele.right)
                    q.append(ele.left)
            level += 1
        return self.out
                
                    

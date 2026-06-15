# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, level):
        if not node:
            return 
        
        if len(self.out) == level:
            self.out.append(node.val)
        
        self.dfs(node.right, level + 1)
        self.dfs(node.left, level + 1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.out = []

        if not root:
            return []
        
        self.dfs(root, 0)
        return self.out
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.maxdia = 0



    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(curr):
            if not curr:
                return 0

            lht = dfs(curr.left)
            rht = dfs(curr.right)

            self.maxdia = max(self.maxdia, lht+rht)
            return 1 + max(lht, rht)
        dfs(root)
        return self.maxdia
    
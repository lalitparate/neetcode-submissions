# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        idx_dict = {}

        for k, v in enumerate(inorder):
            idx_dict[v] = k
        
        self.idx = 0

        def dfs(l, r):
            if l > r:
                return
            
            val = preorder[self.idx]
            self.idx += 1
            root = TreeNode(val)
            midIdx = idx_dict[val]
            root.left = dfs(l, midIdx-1)
            root.right = dfs(midIdx+1, r)
            return root
            
        
        return dfs(0, len(preorder)-1)

        
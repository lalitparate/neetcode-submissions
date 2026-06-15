# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, root, level):
        if not root:
            return
        if len(self.out) == level:
            self.out.append([])
        self.out[level].append(root.val)

        self.bfs(root.left, level + 1)
        self.bfs(root.right, level + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.out = []

        self.bfs(root, 0)

        return self.out

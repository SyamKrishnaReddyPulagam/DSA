# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        ans=[0]
        def bfs(root):
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                nonlocal ans
                ans[0]+=root.left.val
            bfs(root.left)
            bfs(root.right)
        bfs(root)
        return ans[0]
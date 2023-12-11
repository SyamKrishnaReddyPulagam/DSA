# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def func(root):
            if not root:
                return 0
            nonlocal ans
            ans+=1
            func(root.left)
            func(root.right)
            return ans
        ans=0
        return func(root)
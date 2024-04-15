# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        def func(root,sums):
            if not root:
                return
            if root and not root.left and not root.right:
                nonlocal ans
                ans+=sums*10+root.val
            func(root.left,sums*10+root.val)
            func(root.right,root.val+sums*10)
            
        func(root,0)
        return ans
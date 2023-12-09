# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def func(root,maxi):
            if not root:
                return 0
            res=1 if root.val>=maxi else 0
            maxi=max(maxi,root.val)
            res+=func(root.left,maxi)
            res+=func(root.right,maxi)
            return res
        return func(root,root.val)
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        root1=root
        while root1:
            if p.val>root1.val and q.val>root1.val:
                root1=root1.right
            elif p.val<root1.val and q.val<root1.val:
                root1=root1.left
            else:
                return root1
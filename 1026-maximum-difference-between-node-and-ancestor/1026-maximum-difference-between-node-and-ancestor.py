# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ansg = 0
        def help(root, val):
            nonlocal ansg
            if not root:
                return 
            ansg = max(ansg, abs(root.val-val))
            help(root.left, val)
            help(root.right, val)
        def trav(root):
            if not root:
                return
            help(root, root.val)
            trav(root.left)
            trav(root.right)
        trav(root)
        return ansg
            
            
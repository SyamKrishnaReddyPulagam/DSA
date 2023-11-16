# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root1=root
        tmp=root1.left
        root1.left=root1.right
        root1.right=tmp
        self.invertTree(root1.left)
        self.invertTree(root1.right)
        return root
            
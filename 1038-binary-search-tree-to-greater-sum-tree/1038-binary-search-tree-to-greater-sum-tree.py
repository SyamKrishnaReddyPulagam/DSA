# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def func(root):
            if not root:
                return
            if root.right:
                func(root.right)
            ans[0]+=root.val
            #print(ans[0],root.val)
            root.val=ans[0]
            if root.left:
                func(root.left)
            return root
        ans=[0]
        return func(root)
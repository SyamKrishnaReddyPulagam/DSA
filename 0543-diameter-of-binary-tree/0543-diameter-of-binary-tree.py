# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans=0
        self.func(root)
        return self.ans
    def func(self,root):
        if not root:
            return -1
        left=self.func(root.left)
        right=self.func(root.right)
        self.ans=max(self.ans,left+right+2)
        return 1+max(left,right)
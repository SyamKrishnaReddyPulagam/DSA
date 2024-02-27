# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        temp=[]
        def func(root):
            if not root:
                return
            temp.append(root.val)
            func(root.left)
            func(root.right)
        func(root)
        ans=TreeNode(0)
        a=ans
        temp.sort()
        for i in range(len(temp)):
            t=TreeNode(temp[i])
            a.right=t
            a=a.right
        return ans.right
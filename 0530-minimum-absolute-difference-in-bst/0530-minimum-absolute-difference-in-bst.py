# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def func(root):
            if not root:
                return None
            ans.append(root.val)
            func(root.left)
            func(root.right)
        func(root)
        if not root:
            return 0
        ans.sort()
        temp=float("inf")
        for i in range(1,len(ans)):
            temp=min(temp,ans[i]-ans[i-1])
        return temp
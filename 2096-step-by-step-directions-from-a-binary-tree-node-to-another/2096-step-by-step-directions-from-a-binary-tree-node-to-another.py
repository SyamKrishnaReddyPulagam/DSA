# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def func(root,ans,val):
            if not root:
                return ""
            if root.val==val:
                return ans
            ans.append("L")
            left=func(root.left,ans,val)
            if left:
                return left
            ans.pop()
            
            ans.append("R")
            right=func(root.right,ans,val)
            if right:
                return right
            ans.pop()
            
            return ""
        start=func(root,[],startValue)
        end=func(root,[],destValue)
        print(start,end)
        i,n=0,min(len(start),len(end))
        while i<n:
            if start[i]==end[i]:
                i+=1
            else:
                break
        return "U"*len(start[i:])+"".join(end[i:])
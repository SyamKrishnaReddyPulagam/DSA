# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        temp=list(map(chr, range(97, 123)))
        dicti={}
        for i in range(len(temp)):
            dicti[i]=temp[i]
        ans=[]
        def func(root,cur):
            if not root:
                return
            if root and not root.left and not root.right:
                ans.append(dicti[root.val]+cur)
            func(root.left,dicti[root.val]+cur)
            func(root.right,dicti[root.val]+cur)
        func(root,"")
        ans.sort()
        return ans[0]
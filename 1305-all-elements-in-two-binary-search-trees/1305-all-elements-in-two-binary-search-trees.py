# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def func(root,ans):
            if not root:
                return []
            ans.append(root.val)
            if root.left:
                func(root.left,ans)
            if root.right:
                func(root.right,ans)
            return ans
        z1=func(root1,[])
        z2=func(root2,[])
        z1+=z2
        z1.sort()
        return z1
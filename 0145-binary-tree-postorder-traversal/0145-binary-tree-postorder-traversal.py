# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def func(root,ans):
            if not root:
                return
            func(root.left,ans)
            func(root.right,ans)
            ans.append(root.val)
            return ans
        return func(root,[])
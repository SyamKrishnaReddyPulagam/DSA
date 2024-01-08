# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0
        def dfs(root,left,right):
            if not root:
                return 0
            if root.val>=left and root.val<=right:
                nonlocal ans
                ans+=root.val
            dfs(root.left,left,right)
            dfs(root.right,left,right)
            return ans
        return dfs(root,low,high)
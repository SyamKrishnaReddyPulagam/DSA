# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def func(root,dep):
            if not root:
                return
            if dep==depth-1:
                l,r=root.left,root.right
                root.left,root.right=TreeNode(val),TreeNode(val)
                root.left.left,root.right.right=l,r
            func(root.left,dep+1)
            func(root.right,dep+1)
        root1=root
        if depth==1:
            root2=TreeNode(val)
            root2.left=root
            return root2
        func(root1,1)
        return root
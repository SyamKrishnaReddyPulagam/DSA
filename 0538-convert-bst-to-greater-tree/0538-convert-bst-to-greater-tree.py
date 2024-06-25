# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root,ans):
            if not root:
                return
            inorder(root.right,ans)
            ans.append(root.val)
            inorder(root.left,ans)
            return
        temp=[]
        inorder(root,temp)
        dicti,cur_sum={},0
        for i in temp:
            cur_sum+=i
            dicti[i]=cur_sum
        def func(root,dicti):
            if not root:
                return
            root.val=dicti[root.val]
            func(root.left,dicti)
            func(root.right,dicti)
            return root
        return func(root,dicti)
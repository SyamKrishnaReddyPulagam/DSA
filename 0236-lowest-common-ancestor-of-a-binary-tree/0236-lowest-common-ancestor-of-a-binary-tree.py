# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=[]
        def func(temp,root,value):
            if not root:
                return
            if root.val==value:
                temp.append(root.val)
                ans.append(temp.copy())
                return
            temp.append(root.val)
            if root.left:
                func(temp,root.left,value)
            if root.right:
                func(temp,root.right,value)
            temp.pop()
            return
        func([],root,p.val)
        func([],root,q.val)
        a,b=ans[0],ans[1]
        cur=a[0]
        for i in range(1,min(len(a),len(b))):
            if a[i]==b[i]:
                cur=a[i]
            else:
                break
        return TreeNode(cur)
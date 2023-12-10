# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def func(root):
            if not root:
                return
            queue=[root]
            ans=[]
            while queue:
                temp=[]
                z=len(queue)
                for j in range(z):
                    node=queue.pop(0)
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                ans.append(temp)
            return ans
        ans=func(root)
        n=len(ans)
        for i in range(n):
            level=i%2
            if level==0:
                z= sorted(ans[i])
                if ans[i]!=z or len(ans[i])!=len(set(ans[i])):
                    return False
            if level==1:
                z=sorted(ans[i],reverse=True)
                if ans[i]!=z or len(ans[i])!=len(set(ans[i])):
                    return False
            for j in ans[i]:
                if j%2==level:
                    return False
        return True
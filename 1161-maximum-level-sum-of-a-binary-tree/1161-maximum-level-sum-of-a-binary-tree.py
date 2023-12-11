# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            if not root:
                return
            queue=[root]
            ans=[]
            while queue:
                z=len(queue)
                tmp=[]
                for i in range(z):
                    node=queue.pop(0)
                    tmp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                ans.append(tmp)
            return ans
        if not root:
            return 0
        ans=bfs(root)
        sums=float("-inf")
        ind=0
        for i in range(len(ans)):
            a=sum(ans[i])
            if sums<a:
                sums=a
                ind=i
        return ind+1
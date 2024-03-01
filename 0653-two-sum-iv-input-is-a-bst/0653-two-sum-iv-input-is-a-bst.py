# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def bfs(root):
            stack=[root]
            ans=[]
            while stack:
                temp=[]
                for i in range(len(stack)):
                    node=stack.pop(0)
                    temp.append(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                ans+=temp
            return ans
        ans=bfs(root)
        ans.sort()
        i,j=0,len(ans)-1
        while i<j:
            if ans[i]+ans[j]==k:
                return True
            elif ans[i]+ans[j]>k:
                j-=1
            elif ans[i]+ans[j]<k:
                i+=1
        return False
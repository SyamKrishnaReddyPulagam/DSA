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
                ans.append(temp)
            return ans
        nums=bfs(root)
        ans=[]
        for i in nums:
            ans+=i
        if len(ans)<2:
            return False
        for i in range(len(ans)):
            for j in range(i+1,len(ans)):
                if ans[i]+ans[j]==k:
                    return True
        return False
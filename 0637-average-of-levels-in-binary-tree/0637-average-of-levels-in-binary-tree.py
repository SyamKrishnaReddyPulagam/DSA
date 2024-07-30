# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        def func(root):
            queue=deque()
            queue.append(root)
            ans=[]
            while queue:
                temp,count=0,0.0
                for _ in range(len(queue)):
                    node=queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    temp+=node.val
                    count+=1
                ans.append(temp/count)
            return ans
        return func(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        queue=collections.deque()
        queue.append(root)
        
        while queue:
            length=len(queue)
            cache=[]
            for i in range(length):
                top=queue.popleft()
                if top:
                    cache.append(top.val)
                    queue.append(top.left)
                    queue.append(top.right)
            if cache:
                ans.append(cache)
        return ans
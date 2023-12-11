# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
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
            return []
        ans=bfs(root)
        return [max(i) for i in ans]
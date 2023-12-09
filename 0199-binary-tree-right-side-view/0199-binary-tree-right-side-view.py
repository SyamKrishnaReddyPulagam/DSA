# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def func(root):
            if not root:
                return
            nonlocal res
            queue=[root]
            while queue:
                level_size = len(queue)
                current_level = []
                for i in range(level_size):
                    node = queue.pop(0)
                    current_level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                res.append(current_level)
                
        func(root)
        ans=[]
        for i in res:
            ans.append(i[-1])
        return ans
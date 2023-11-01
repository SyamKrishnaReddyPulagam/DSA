# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        deque = [root]
        d = {}
        while deque:
            item = deque.pop()
            if item.val not in d:
                d[item.val] = 1
            else:
                d[item.val] += 1
            if item.left:
                deque.append(item.left)
            if item.right:
                deque.append(item.right)
        l = sorted(d.keys(), key = lambda x: d[x])
        m = max(d.values())
        result = []
        for i in l[::-1]:
            if d[i] == m:
                result.append(i)
            else:
                break
        return result
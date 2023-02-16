class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        left_depth = 1+self.maxDepth(root.left)
        right_depth = 1+self.maxDepth(root.right)
        p=max(left_depth, right_depth)
        return p
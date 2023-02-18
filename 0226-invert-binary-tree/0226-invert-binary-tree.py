class Solution(object):
    def invertTree(self, root):
        root1=root
        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root1.left, root1.right = root.right, root.left
        return root1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(node):
            while node.left:
                node = node.left
            return node

        def delete(root, key):
            if not root:
                return None

            if key < root.val:
                root.left = delete(root.left, key)
            elif key > root.val:
                root.right = delete(root.right, key)
            else:
                if not root.left and not root.right:
                    root = None
                elif not root.left:
                    root = root.right
                elif not root.right:
                    root = root.left
                else:
                    min_node = findMin(root.right)
                    root.val = min_node.val
                    root.right = delete(root.right, min_node.val)
            return root

        return delete(root, key)
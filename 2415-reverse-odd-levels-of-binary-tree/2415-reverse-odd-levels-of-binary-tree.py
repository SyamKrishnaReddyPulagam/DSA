# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        queue = deque([(root, 0)])  # Queue to perform level-order traversal
        levels = {}  # Dictionary to store nodes at each level

        # Traverse the tree level by level
        while queue:
            node, level = queue.popleft()
            if level not in levels:
                levels[level] = []
            levels[level].append(node)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        # Swap nodes at odd levels
        for level, nodes in levels.items():
            if level % 2 != 0:
                for i in range(len(nodes) // 2):
                    nodes[i].val, nodes[-i - 1].val = nodes[-i - 1].val, nodes[i].val

        return root
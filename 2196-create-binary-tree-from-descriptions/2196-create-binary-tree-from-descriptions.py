# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dicti={}
        nodes,tot=set(),set()
        for i in descriptions:
            ind=0 if i[2] else 1
            if i[0] in dicti:
                dicti[i[0]][ind]=i[1]
            else:
                dicti[i[0]]=[None,None]
                dicti[i[0]][ind]=i[1]
            nodes.add(i[1])
            tot.add(i[1])
            tot.add(i[0])
        head=(list(tot-nodes))[0]
        for i in tot:
            if i not in dicti:
                dicti[i]=[None,None]
        def func(dicti,node):
            if not node or node not in dicti:
                return None
            root=TreeNode(node)
            root.left=func(dicti,dicti[node][0])
            root.right=func(dicti,dicti[node][1])
            return root
        return func(dicti,head)
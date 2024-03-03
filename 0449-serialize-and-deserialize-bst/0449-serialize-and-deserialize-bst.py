# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(root):
            if not root:
                return
            self.ans+=str(root.val)+" "
            preorder(root.left)
            preorder(root.right)
        self.ans=""
        preorder(root)
        return self.ans
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr=[]
        for i in data.split(" "):
            if i!="":
                arr.append(int(i))
        def insert(root,val):
            if not root:
                return TreeNode(val)
            if val<root.val:
                root.left=insert(root.left,val)
            else:
                root.right=insert(root.right,val)
            return root
        root=None
        for i in arr:
            root=insert(root,i)
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
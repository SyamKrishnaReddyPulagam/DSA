# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root,arr):
            if not root:
                return
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
            return arr
        arr=inorder(root,[])
        def func(arr,l,r):
            if l>r:
                return None
            mid=(l+r)//2
            node=TreeNode(arr[mid])
            node.left=func(arr,l,mid-1)
            node.right=func(arr,mid+1,r)
            return node
        return func(arr,0,len(arr)-1)
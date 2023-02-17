class Solution(object):
    def minDiffInBST(self, root):
        x=[]
        def inorderTraversal(root):
            if root:
                inorderTraversal(root.left)
                x.append(root.val)
                inorderTraversal(root.right)
        inorderTraversal(root)
        minimum=1000
        for i in range(1,len(x)):
            minimum=min(minimum,x[i]-x[i-1])
        return minimum
    
        
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k==1:
            return n
        root1=ListNode(0)
        root=root1
        for i in range(1,n+1):
            root1.next=ListNode(i)
            root1=root1.next
        root=root.next
        root1.next=root
        while root and root.val!=root.next.val:
            for i in range(k-2):
                root=root.next
            print(root.next.val)
            root.next=root.next.next   
            root=root.next
        return root.val
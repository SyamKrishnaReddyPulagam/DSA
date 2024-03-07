# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def leng(root):
            a=0
            while root:
                a+=1
                root=root.next
            return a
        root=head
        n=(leng(root))//2
        while n>0:
            root=root.next
            n-=1
        return root
        
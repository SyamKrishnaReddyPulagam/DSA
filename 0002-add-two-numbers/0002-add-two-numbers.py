# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        while l1:
            s1+=str(l1.val)
            l1=l1.next
        s1=s1[::-1]
        
        s2=""
        while l2:
            s2+=str(l2.val)
            l2=l2.next
        s2=s2[::-1]
        s1=int(s1)
        s2=int(s2)
        s3=str(s1+s2)
        s3=s3[::-1]
        l3=ListNode(0)
        l4=l3
        for i in range(len(s3)):
            a=int(s3[i])
            l3.next=ListNode(a)
            l3=l3.next
        l3.next=None
        return l4.next
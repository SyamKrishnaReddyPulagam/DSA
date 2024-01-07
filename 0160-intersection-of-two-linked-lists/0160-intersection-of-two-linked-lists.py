# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1,l2=headA,headB
        def length(head1):
            x=0
            while head1:
                x+=1
                head1=head1.next
            return x
        def func(head1,diff):
            while diff!=0:
                head1=head1.next
                diff-=1
            return head1
        m,n=length(headA),length(headB)
        diff=abs(m-n)
        if m>n:
            l1=func(l1,diff)
        elif m<n:
            l2=func(l2,diff)
        while l1 and l2:
            if l1==l2:
                return l1
            l1=l1.next
            l2=l2.next
        return None
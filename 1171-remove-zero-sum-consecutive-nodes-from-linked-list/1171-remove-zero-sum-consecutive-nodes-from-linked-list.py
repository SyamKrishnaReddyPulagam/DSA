# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1001)
        dummy.next=head
        dicti={}
        dicti[0]=dummy
        sums=0
        
        while(head):
            sums+=head.val
            if sums in dicti:
                temp=dicti[sums].next
                a=sums
                while temp!=head:
                    a+=temp.val
                    del dicti[a]
                    temp=temp.next
                dicti[sums].next=head.next
            else:
                dicti[sums]=head
            head=head.next
        return dummy.next
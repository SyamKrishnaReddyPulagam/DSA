# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reversed(list1):
            prev=None
            curr=list1
            while curr:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        list1=head
        list2=head
        while list1 and list1.next:
            list1=list1.next.next
            list2=list2.next
        list3=reversed(list2)
        list4=head
        x=0
        while list3:
            x=max(x,list3.val+list4.val)
            list3=list3.next
            list4=list4.next
        return x
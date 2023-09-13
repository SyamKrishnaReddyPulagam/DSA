# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        length=0
        list1=head
        list2=head
        while list1:
            length+=1
            list1=list1.next
        mid=length//2
        x=0
        if mid==0:
            return None
        prev=None
        while x<mid:
            prev=list2
            list2=list2.next
            x+=1
        if list2.next:
            prev.next=list2.next
        else:
            prev.next=None
        return head
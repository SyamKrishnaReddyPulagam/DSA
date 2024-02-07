# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        list1=ListNode(0)
        root=list1
        while head:
            if head.val!=val:
                list1.next=ListNode(head.val)
                list1=list1.next
            head=head.next
        return root.next
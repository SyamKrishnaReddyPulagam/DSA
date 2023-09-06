# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return None
        x=head.next
        o,e=head,x
        while e and e.next:
            o.next=e.next
            o=o.next
            e.next=o.next
            e=e.next
        o.next=x
        return head
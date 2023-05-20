# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):  
        x = head
        while x:
            while x.next and x.next.val == x.val:
                x.next = x.next.next     
            x = x.next     
        return head
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or head.next==None:
            return False
        
        x = head
        y = head
        
        while y != None and y.next != None:
            x = x.next
            y = y.next.next
            
            if x == y:
                return True
        
        return False
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """objective----> lprev stores nodes before left
                          prev will makes changes between left and right and will be required head of that part to be added to lprev
                          curr will have all nodes after right 
           """
        if not head:
            return None
        if left==right:
            return head
        list1=ListNode(0)
        list1.next=head
        lprev,curr=list1,head
        #nodes before left are stored in lprev
        for i in range(left-1):
            lprev,curr=curr,curr.next
        #nodes between left and right
        prev=None
        for i in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev,curr=curr,temp
        #now joining each other parts of linkedlist to combine to one
        lprev.next.next=curr #linkedlist after right
        lprev.next=prev #linkedlist between left and right including
        return list1.next
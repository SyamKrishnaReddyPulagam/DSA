# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return None
        if head.next==None:
            return head
        def length1(head):
            i=1
            while head.next!=None:
                head=head.next
                i+=1
            return i
        def rotate(head):
            dummy2=head
            while head.next.next!=None:
                head=head.next
            temp=head.next.val
            head.next=None
            dummy=ListNode(temp)
            dummy.next=dummy2
            return dummy
        x=length1(head)
        k=k%x
        for i in range(k):
            head=rotate(head)
        return head
            
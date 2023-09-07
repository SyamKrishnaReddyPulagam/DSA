# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        n=0
        x=head
        while x:
            n+=1
            x=x.next
        y=head
        for i in range(n//2):
            y=y.next
        z=y
        def reverse(head):
            list1=head
            prev=None
            while list1:
                temp=list1.next
                list1.next=prev
                prev,list1=list1,temp
            return prev
        #print(head)
        list1=reverse(z)
        #print(list1)
        while list1:
            if head.val!=list1.val:
                return False
            head=head.next
            list1=list1.next
        #print(list1)
        return True
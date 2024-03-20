# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        n=1
        root1=list1
        while n<a:
            root1=root1.next
            n+=1
        root2=root1.next
        root1.next=list2
        while n<=b:
            root2=root2.next
            n+=1
        while root1.next:
            root1=root1.next
        root1.next=root2
        return list1
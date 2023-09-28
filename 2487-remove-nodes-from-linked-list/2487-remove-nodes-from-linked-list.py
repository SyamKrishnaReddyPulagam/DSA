# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reversed(list1):
            prev=None
            while list1: 
                temp=list1.next
                list1.next=prev
                prev=list1
                list1=temp
            return prev
        list2 = head
        list1 = reversed(list2)
        list3 = ListNode(0)
        maxi = float("-inf")
        list4=list3
        while list1:
            if list1.val >= maxi:
                maxi = list1.val
                new_node = ListNode(list1.val)
                new_node.next = list3.next
                list3.next = new_node
                list3=list3.next
            list1 = list1.next
        return reversed(list4.next)
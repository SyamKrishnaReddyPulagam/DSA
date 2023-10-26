# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        list5=head
        while list5:
            arr.append(list5.val)
            list5=list5.next
        arr.sort()
        list1=ListNode(0)
        list2=list1
        for i in arr:
            list1.next=ListNode(i)
            list1=list1.next
        return list2.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=ListNode(0)
        z=l
        list1=head
        arr=[]
        while list1:
            arr.append(list1.val)
            list1=list1.next
        arr=sorted(arr)
        for i in range(len(arr)):
            x=ListNode(arr[i])
            l.next=x
            l=l.next
        return z.next
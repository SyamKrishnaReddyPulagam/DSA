# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1=head
        list2=head
        pos=ListNode(-1)
        while list2 and list2.next:
            list1=list1.next
            list2=list2.next.next
            if list1==list2:
                list1 = head
                while list1!= list2:
                    list1 = list1.next
                    list2 = list2.next
                return list1
        return None
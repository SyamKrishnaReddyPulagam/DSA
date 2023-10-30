# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next==None:
            return head
        list2=ListNode(head.val)
        list1=head.next
        def manip(list1,val):
            list3=list1
            if val<list3.val:
                x=ListNode(val)
                x.next=list3
                return x
            else:
                while list3.next and list3.next.val<val:
                    list3=list3.next
                temp=list3.next
                list3.next=ListNode(val)
                list3=list3.next
                list3.next=temp
                return list1
        while list1:
            list2=manip(list2,list1.val)
            #print(list2)
            list1=list1.next
        return list2
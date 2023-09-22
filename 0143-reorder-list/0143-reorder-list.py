# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None
        prev = None
        curr = second_half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        first_half = head
        second_half = prev
        while second_half:
            temp1 = first_half.next
            temp2 = second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2

        return head
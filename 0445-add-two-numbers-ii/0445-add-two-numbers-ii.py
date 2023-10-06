class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_length(list1):
            n = 0
            while list1:
                n += 1
                list1 = list1.next
            return n
        def reverse_list(head1):
            prev = None
            list1 = head1
            while list1:
                temp = list1.next
                list1.next = prev
                prev = list1
                list1 = temp
            return prev
        
        ans = ListNode(0)
        new = ans
        carry = 0
        list1 = reverse_list(l1)
        list2 = reverse_list(l2)
        while list1 or list2:
            val1 = list1.val if list1 else 0
            val2 = list2.val if list2 else 0
            x = val1 + val2 + carry
            carry = x // 10
            x %= 10
            node = ListNode(x)
            ans.next = node
            ans = ans.next
            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next
        if carry != 0:
            ans.next = ListNode(carry)
        return reverse_list(new.next)
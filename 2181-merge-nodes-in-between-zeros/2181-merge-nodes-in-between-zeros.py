# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,ans=0,[]
        while head:
            if head.val==0:
                ans.append(temp)
                temp=0
            temp+=head.val
            head=head.next
        ans=ans[1:]
        root=ListNode(0)
        root1=root
        for i in ans:
            root.next=ListNode(i)
            root=root.next
        return root1.next
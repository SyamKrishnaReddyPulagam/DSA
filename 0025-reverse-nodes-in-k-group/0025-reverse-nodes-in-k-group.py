# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans=[]
        while head:
            ans.append(head.val)
            head=head.next
        n=len(ans)
        for i in range(0,n,k):
            if i+k<=n:
                ans[i:i+k]=ans[i:i+k][::-1]
        root=ListNode(0)
        root1=root
        for i in ans:
            root.next=ListNode(i)
            root=root.next
        return root1.next
        
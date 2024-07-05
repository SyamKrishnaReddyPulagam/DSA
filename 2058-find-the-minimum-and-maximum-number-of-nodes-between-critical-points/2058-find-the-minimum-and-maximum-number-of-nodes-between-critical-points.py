# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev,last,cur,first,ind=0,-1,-1,-1,0
        ans=[float("inf"),float("-inf")]
        while head and head.next:
            if prev!=0 and head.val>prev and head.val>head.next.val:
                last=cur
                cur=ind
                if first==-1:
                    first=ind
                if last!=-1:
                    ans[0]=min(ans[0],cur-last)
                    ans[1]=max(ans[1],cur-first)
            elif prev!=0 and head.val<prev and head.val<head.next.val:
                last=cur
                cur=ind
                if first==-1:
                    first=ind
                if last!=-1:
                    ans[0]=min(ans[0],cur-last)
                    ans[1]=max(ans[1],cur-first)
            ind+=1
            prev=head.val
            head=head.next
        if ans==[float("inf"),float("-inf")]:
            return [-1,-1]
        return ans
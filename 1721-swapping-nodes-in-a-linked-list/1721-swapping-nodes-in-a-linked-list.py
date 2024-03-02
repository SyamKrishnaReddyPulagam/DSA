# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        arr=[]
        root=head
        while root:
            arr.append(root.val)
            root=root.next
        n=len(arr)
        def make(arr,root):
            for i in range(len(arr)):
                if not root:
                    root=ListNode(arr[i])
                    ans=root
                else:
                    root.next=ListNode(arr[i])
                    root=root.next
            if not root:
                return None
            return ans
        arr[k-1],arr[-k]=arr[-k],arr[k-1]
        return make(arr,None)
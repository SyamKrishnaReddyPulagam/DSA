# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        hlist=head
        n=0
        while hlist!=None:
            n+=1
            hlist=hlist.next
        nsize=n/k
        esize=n%k
        if k>n:
            nsize=1
            esize=0
        list1=head
        a=[]
        for i in range(k):
            part_head=list1
            part_end=None
            if esize>0:
                usize=nsize+1
            else:
                usize=nsize
            for i in range(usize):
                if list1:
                    part_end=list1
                    list1=list1.next
            if part_end:
                part_end.next=None
            a.append(part_head)
            esize-=1
        return a
                
            
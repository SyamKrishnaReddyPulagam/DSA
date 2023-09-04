# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """def mergelist(self, list1, list2):
            dummy = curr = ListNode(0)   
            while list1 and list2:
                if list1.val<list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            if list1:
                curr.next = list1
            if list2 :
                curr.next = list2
            return dummy.next
        if not lists:
            return None
        if len(lists)==1:
                return lists[0]
        mergedlist=[]
        mergedlist.append(lists[0])
        for i in range(1,len(lists)):
            l1=mergedlist[0]
            l2=lists[i]
            mergedlist[0]=mergelist(self,l1,l2)
        return mergedlist[0]"""
        
        #using priority queue to solve this
        h=[]
        
        one=two=ListNode(0)
        
        for i,x in enumerate(lists):
            if x:
                heappush(h,(x.val,i))
        while h:
            val,i=heappop(h)
            two.next=ListNode(val)
            if lists[i].next:
                lists[i]=lists[i].next
                heappush(h,(lists[i].val,i))
            two=two.next
        return one.next
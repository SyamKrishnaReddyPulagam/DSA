class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        n,tot=len(capacity),sum(apple)
        ans,i=0,n-1
        while tot>0 and i>=0:
            tot-=capacity[i]
            ans+=1
            i-=1
        return ans
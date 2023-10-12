# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int,nums: 'MountainArray') -> int:
        length=nums.length()
        start,end=1,length-2
        while start<=end:
            mid=(start+end)//2
            a,b,c=nums.get(mid-1),nums.get(mid),nums.get(mid+1)
            if a<b and b<c:
                start=mid+1
            elif a>b and b>c:
                end=mid-1
            else:
                break
        i,j=0,mid
        while i<=j:
            k=(i+j)//2
            if nums.get(k)==target:
                return k
            elif nums.get(k)<target:
                i=k+1
            else:
                j=k-1
        i,j=mid,length-1
        while i<=j:
            k=(i+j)//2
            if nums.get(k)==target:
                return k
            elif nums.get(k)<target:
                j=k-1
            else:
                i=k+1
        return -1
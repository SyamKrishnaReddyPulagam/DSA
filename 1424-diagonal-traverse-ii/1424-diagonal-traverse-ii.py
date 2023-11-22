class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans=[]
        n=len(nums)
        if n==1:
            return [x for x in nums[0]]
        for i in range(n-1,-1,-1):
            cache=[]
            z=nums[i]
            for j in range(len(z)):
                ans.append((i+j,i,z[j]))
        ans.sort(key=lambda x: (x[0], -x[1]))
        fi=[]
        for i in ans:
            fi.append(i[2])
        return fi
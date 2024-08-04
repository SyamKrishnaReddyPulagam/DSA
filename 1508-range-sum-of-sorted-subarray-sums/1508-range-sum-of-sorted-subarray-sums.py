class Solution(object):
    def rangeSum(self, nums, n, left, right):
        sums=[]
        for i in range(n):
            temp=nums[i]
            sums.append(nums[i])
            for j in range(i+1,n):
                temp+=nums[j]
                sums.append(temp)
        sums.sort()
        return (sum(sums[left-1:right]))%(10**9+7)
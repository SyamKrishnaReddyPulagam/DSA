class Solution(object):
    def minSwaps(self, nums):
        dicti=Counter(nums)
        window=dicti[1]
        nums=nums+nums
        n=len(nums)
        temp,ones=[],0
        for i in nums:
            if i==1:
                ones+=1
            temp.append(ones)
        ans=len(nums)
        for i in range(n-window):
            left,right=i,i+window
            one=temp[right]-temp[left]
            if nums[left]==1:
                one+=1
            if nums[right]==1:
                one-=1
            ans=min(ans,window-one)
        return ans
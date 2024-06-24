class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        temp=deque()
        ans=0
        for i in range(len(nums)):
            while temp and i>temp[0]+k-1:
                temp.popleft()
            if (nums[i]+len(temp))%2==0:
                if i+k>len(nums):
                    return -1
                ans+=1
                temp.append(i)
        return ans
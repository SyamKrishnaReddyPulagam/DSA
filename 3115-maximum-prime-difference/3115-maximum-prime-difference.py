class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=max(nums)
        prime=[True for i in range(maxi+1)]
        prime[0],prime[1]=False,False
        for i in range(2,maxi+1):
            if prime[i]==True:
                x=i*2
                while x<=maxi:
                    prime[x]=False
                    x+=i
        i,j=0,n-1
        while i<=j:
            if prime[nums[i]] and prime[nums[j]]:
                return abs(j-i)
            if not prime[nums[i]]:
                i+=1
            if not prime[nums[j]]:
                j-=1
        return 0
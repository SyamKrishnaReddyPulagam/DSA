class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left,right={},{}
        for i in nums:
            if i in right:
                right[i]+=1
            else:
                right[i]=1
        mod,ans=10**9+7,0
        for i in nums:
            right[i]-=1
            if i*2 not in left or i*2 not in right:
                if i in left:
                    left[i]+=1
                else:
                    left[i]=1
                continue
            else:
                ans+=(left[i*2]*right[i*2])%mod
            if i in left:
                left[i]+=1
            else:
                left[i]=1
            #left[i]=left.get(i,0)+1
            if not right[i]:
                del right[i]
        return ans%mod
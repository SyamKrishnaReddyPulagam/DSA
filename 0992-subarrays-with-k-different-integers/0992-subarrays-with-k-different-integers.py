class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count1 = 0
        count2 = 0

        left = 0
        right = 0

        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        res = 0

        for i in range(len(nums)):
            #count frequencies which are greater than k
            if freq1[nums[i]] == 0:
                count1 +=1
            freq1[nums[i]] +=1
            #Count frequencies which are exactly k
            if freq2[nums[i]] == 0:
                count2 +=1
            freq2[nums[i]] +=1
            
            #Checking for count greater than k
            while count1 > k:
                freq1[nums[right]] -=1
                if freq1[nums[right]] == 0:
                    count1-=1
                right +=1
            
            #Checking Counts for exact k
            while count2 > k-1:
                freq2[nums[left]] -=1
                if freq2[nums[left]] == 0:
                    count2 -=1
                left +=1
            
            res += left - right
        
        return res

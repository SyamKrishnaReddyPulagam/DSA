class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        from sortedcontainers import SortedDict
        dicti={}
        for i in range(len(mapping)):
            dicti[str(i)]=str(mapping[i])
        arr={}
        for i in range(len(nums)):
            cur=str(nums[i])
            new=""
            for j in cur:
                new+=dicti[j]
            arr[nums[i]]=int(new)
        nums.sort(key=lambda x:arr[x])
        return nums
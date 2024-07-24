class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        from sortedcontainers import SortedDict
        dicti={}
        for i in range(len(mapping)):
            dicti[str(i)]=str(mapping[i])
        arr=[]
        for i in range(len(nums)):
            cur=str(nums[i])
            new=""
            for j in cur:
                new+=dicti[j]
            arr.append(int(new))
        temp=SortedDict()
        for i in range(len(arr)):
            if arr[i] in temp:
                temp[arr[i]].append(nums[i])
            else:
                temp[arr[i]]=[nums[i]]
        i=0
        for j in temp:
            for k in temp[j]:
                nums[i]=k
                i+=1
        return nums
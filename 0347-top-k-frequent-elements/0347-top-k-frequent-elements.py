class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset=Counter(nums)
        arr=[]
        for i in hashset:
            arr.append([hashset[i],i])
        arr.sort()
        ans=[]
        j=-1
        for i in range(k):
            ans.append(arr[j][1])
            j-=1
        return ans
        
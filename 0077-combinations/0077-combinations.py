class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=[i+1 for i in range(n)]
        subsets=[[arr[0]]]
        for i in range(1,len(arr)):
            ele=arr[i]
            ap=[[ele]]
            for j in subsets:
                ap.append(j+[ele])
            subsets+=ap
        ans=[]
        for i in subsets:
            if len(i)==k:
                ans.append(i)
        return ans
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        temp=[[i,j] for i,j in zip(difficulty,profit)]
        temp.sort()
        for i in range(1,len(temp)):
            temp[i][1]=max(temp[i-1][1],temp[i][1])
        ans,n=0,len(temp)
        worker.sort()
        index=0
        for i in worker:
            while index<n and temp[index][0]<=i:
                index+=1
            if index<=n and index!=0:
                ans+=temp[index-1][1]
        return ans
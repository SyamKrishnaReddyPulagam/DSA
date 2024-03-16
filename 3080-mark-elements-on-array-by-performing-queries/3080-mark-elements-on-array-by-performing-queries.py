class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        temp1=set()
        temp2=[[nums[i],i] for i in range(len(nums))]
        #temp2.sort(key=lambda x:[x[0],[1]])
        heapq.heapify(temp2)
        ans,j,tot=[],0,sum(nums)
        for i in queries:
            sums=0
            if i[0] not in temp1:
                sums+=nums[i[0]]
                temp1.add(i[0])
            k=i[1]
            while k>0:
                if temp2:
                    x=heapq.heappop(temp2)
                    if x[1] not in temp1:
                        sums+=x[0]
                        temp1.add(x[1])
                        k-=1
                else:
                    break
            tot=max(0,tot-sums)
            ans.append(tot)
        return ans
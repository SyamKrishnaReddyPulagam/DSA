class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        temp=[[i,j] for j,i in zip(customers,grumpy)]
        notGrumpy=0
        for i in temp:
            if i[0]==0:
                notGrumpy+=i[1]
        left,right,winsum,maxsum,n=0,0,0,0,len(temp)
        while right<minutes:
            if temp[right][0]==1:
                winsum+=temp[right][1]
            right+=1
        maxsum=max(maxsum,winsum)
        while right<n:
            if temp[left][0]==1:
                winsum-=temp[left][1]
            left+=1
            if temp[right][0]==1:
                winsum+=temp[right][1]
            right+=1
            maxsum=max(maxsum,winsum)
        #print(notGrumpy,maxsum)
        return notGrumpy+maxsum
            
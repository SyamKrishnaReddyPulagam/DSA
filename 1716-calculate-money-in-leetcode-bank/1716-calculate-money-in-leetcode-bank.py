class Solution:
    def totalMoney(self, n: int) -> int:
        arr=[0]*n
        arr[0]=1
        ans=arr[0]
        cache=0
        for i in range(1,n):
            if i==cache+7:
                arr[i]=arr[cache]+1
                cache=i
            else:
                arr[i]=arr[i-1]+1
            ans+=arr[i]
        return ans
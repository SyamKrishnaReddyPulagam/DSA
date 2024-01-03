class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr=[bank[i].count("1") for i in range(len(bank))]
        ans=0
        for i in range(len(bank)):
            curr=arr[i]
            j=i+1
            while j<len(bank) and arr[j]==0:
                j+=1
            if j<len(bank):
                ans+=(curr*arr[j])
        return ans
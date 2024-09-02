class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i,n=0,len(chalk)
        temp=sum(chalk)
        k=k%temp
        while k>=chalk[i]:
            k-=chalk[i]
            i+=1
            if i==n:
                i=0
        return i
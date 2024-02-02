class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits="123456789"
        n1=len(str(low))
        n2=len(str(high))
        res=[]
        def func(size,low,high):
            n=9
            i=0
            tep=[]
            while i<n-size+1:
                q=int(digits[i:i+size])
                if q>=low and q<=high:
                    tep.append(q)
                i+=1
            return tep
        if n1>9:
            return 0
        for i in range(n1,n2+1):
            size_i_num=func(i,low,high)
            if size_i_num:
                res+=size_i_num
        return res
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        n=len(s)
        if numRows>=n:
            return s
        arr=[""]*numRows
        i,j=0,0
        gdown=1
        gup=0
        while i<n and j<numRows:
            arr[j]+=s[i]
            #print(arr)
            i+=1
            if j==0 and gup==1:
                gdown=1
                gup=0
                j+=1
            elif j==numRows-1 and gdown==1:
                gdown=0
                gup=1
                j-=1
            else:
                if gdown==1:
                    j+=1
                else:
                    j-=1
        return "".join(arr)
            
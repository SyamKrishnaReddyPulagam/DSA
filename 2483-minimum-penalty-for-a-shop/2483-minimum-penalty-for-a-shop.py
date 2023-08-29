class Solution(object):
    def bestClosingTime(self, customers):
        n=len(customers)
        prefix=[0]*(len(customers)+1)
        postfix=[0]*(len(customers)+1)
        
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]
            if customers[i-1]=='N':
                prefix[i]+=1
        for i in range(n-1,-1,-1):
            postfix[i]=postfix[i+1]
            if customers[i]=="Y":
                postfix[i]+=1
        
        min_penalty=float("inf")
        index=0
        for i in range(n+1):
            a=postfix[i]+prefix[i]
            if a<min_penalty:
                min_penalty=a
                index=i
        return index
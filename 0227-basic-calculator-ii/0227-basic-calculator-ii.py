class Solution:
    def calculate(self, s: str) -> int:
        i=0
        prev,curr,tot=0,0,0
        tsum=0
        curr_opr="+"
        while i<len(s):
            curr=s[i]
            if curr.isdigit():
                while i<len(s) and s[i].isdigit():
                    tsum=tsum*10+int(s[i])
                    i+=1
                i-=1
                if curr_opr=="+":
                    tot+=tsum
                    prev=tsum
                elif curr_opr=="-":
                    tot-=tsum
                    prev=-tsum
                elif curr_opr=="*":
                    tot-=prev
                    tot+=prev*tsum
                    prev=prev*tsum
                else:
                    tot-=prev
                    tot+=int(prev/tsum)
                    prev=int(prev/tsum)
                    
                tsum=0
                    
            elif curr!=" ":
                curr_opr=curr
            i+=1
        return tot
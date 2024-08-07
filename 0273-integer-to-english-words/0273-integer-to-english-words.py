class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        one = {1: ["One","Ten","One Hundred"],2: ["Two","Twenty","Two Hundred"],3: ["Three","Thirty","Three Hundred"],4: ["Four","Forty","Four Hundred"],5: ["Five","Fifty","Five Hundred"],6: ["Six","Sixty","Six Hundred"],7: ["Seven","Seventy","Seven Hundred"],8: ["Eight","Eighty","Eight Hundred"],9: ["Nine","Ninety","Nine Hundred"],11:["Eleven"],12:["Twelve"],13:["Thirteen"],14:["Fourteen"],15:["Fifteen"],16:["Sixteen"],17:["Seventeen"],18:["Eighteen"],19:["Nineteen"]}
        def func(word,one): #word="123"
            
            temp=""
            if len(word) != 3:
                word = "0" * (3 - len(word)) + word
            if word[0]!="0":
                temp+=one[int(word[0])][-1]
                
            if word[1]!="1" and word[1]!="0":
                if temp:
                    temp+=" "
                temp+=one[int(word[1])][-2]
            if word[1]=="1":
                if temp:
                    temp+=" "
                if word[2]=="0":
                    temp+="Ten"
                else:
                    temp+=one[int(word[1:])][0]
                return temp
                
            if word[2]!="0":
                if temp:
                    temp+=" "
                temp+=one[int(word[2])][0]
            return temp
        num=str(num)
        temp=["Billion","Million","Thousand",""]
        ans=""
        arr =[num[i-3:i] for i in range(len(num),2,-3)]
        arr.append(num[:len(num)%3])
        ind=-1
        for i in arr:
            if not i:
                continue
            temp1=func(i,one)
            if not temp1:
                ind-=1
                continue
            temp1+=" "+temp[ind]
            ind-=1
            if ans:
                ans=temp1+" "+ans
            else:
                ans=temp1
        if ans[-1]==" ":
            return ans[:-1]
        return ans

class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        one={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
        ten={1:"Ten",2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
        hundred={1:"One Hundred",2:"Two Hundred",3:"Three Hundred",4:"Four Hundred",5:"Five Hundred",6:"Six Hundred",7:"Seven Hundred",8:"Eight Hundred",9:"Nine Hundred"}
        special={11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
        def func(word,one,ten,hundred): #word="123"
            
            temp=""
            if len(word) != 3:
                word = "0" * (3 - len(word)) + word
            if word[0]!="0":
                temp+=hundred[int(word[0])]
                
            if word[1]!="1" and word[1]!="0":
                if temp:
                    temp+=" "
                temp+=ten[int(word[1])]
            if word[1]=="1":
                if temp:
                    temp+=" "
                if word[2]=="0":
                    temp+="Ten"
                else:
                    temp+=special[int(word[1:])]
                return temp
                
            if word[2]!="0":
                if temp:
                    temp+=" "
                temp+=one[int(word[2])]
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
            temp1=func(i,one,ten,hundred)
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

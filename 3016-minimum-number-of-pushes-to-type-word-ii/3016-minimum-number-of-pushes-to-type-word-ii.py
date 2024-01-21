class Solution:
    def minimumPushes(self, word: str) -> int:
        def func1(word):
            dicti2=Counter(word)
            dicti3 = dict(sorted(dicti2.items(), key=lambda x: -x[1]))
            key,counter,ans=1,0,0
            for i in dicti3:
                ans+=dicti3[i]*key
                counter+=1
                if counter==8:
                    key+=1
                    counter=0
            return ans
                
        nums=list(word)
        return func1(word)
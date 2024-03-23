class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        dicti2={}
        for i in words2:
            dic=Counter(i)
            for i in dic:
                if i in dicti2:
                    dicti2[i]=max(dicti2[i],dic[i])
                else:
                    dicti2[i]=dic[i]
        ans=[]
        def func(dic1,dic2):
            for i in dic2:
                if i not in dic1 or (dic1[i]<dic2[i]):
                    return False
            return True
        for i in range(len(words1)):
            w=Counter(words1[i])
            if func(w,dicti2):
                ans.append(words1[i])
        return ans
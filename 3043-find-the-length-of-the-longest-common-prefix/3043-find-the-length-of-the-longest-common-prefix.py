class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        dicti={}
        for i in range(len(arr1)):
            num=str(arr1[i])
            ele_len=len(num)
            i=1
            while i<=ele_len:
                if num[:i] not in dicti:
                    dicti[num[:i]]=0
                i+=1
        arr2.sort(key= lambda x:-len(str(x)))
        ans=0
        for i in range(len(arr2)):
            num=str(arr2[i])
            while num:
                if num in dicti:
                    ans=max(ans,len(num))
                    break
                else:
                    num=num[:-1]
        return ans
            
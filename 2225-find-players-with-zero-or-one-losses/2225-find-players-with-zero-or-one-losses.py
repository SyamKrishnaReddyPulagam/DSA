class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans=[]
        win,nlost=[],[]
        temp=set()
        dicti={}
        for i in matches:
            temp.add(i[0])
            temp.add(i[1])
            if i[1] in dicti:
                dicti[i[1]]+=1
            else:
                dicti[i[1]]=1
        for i in temp:
            if i not in dicti:
                win.append(i)
        for i in dicti:
            if dicti[i]==1:
                nlost.append(i)
        ans.append(sorted(win))
        ans.append(sorted(nlost))
        return ans
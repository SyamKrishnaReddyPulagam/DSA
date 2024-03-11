class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dicti=Counter(s)
        ans=""
        for i in range(len(order)):
            if order[i] in dicti:
                ans+=order[i]*dicti[order[i]]
                del dicti[order[i]]
        for i in dicti:
            ans+=i*dicti[i]
        return ans
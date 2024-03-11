class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dicti=Counter(s)
        ans=""
        for i in range(len(order)):
            if order[i] in dicti:
                ans+=order[i]*dicti[order[i]]
        order,s=set(order),set(s)
        s=s-order
        for i in s:
            ans+=i*dicti[i]
        return ans
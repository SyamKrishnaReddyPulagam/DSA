class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cur=0
        for i in logs:
            if i=="../":
                cur=max(0,cur-1)
            elif i=="./":
                continue
            else:
                cur+=1
        return cur
                    
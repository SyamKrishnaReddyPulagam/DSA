class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sgas,scost=sum(gas),sum(cost)
        if scost>sgas:
            return -1
        tot,ans=0,0
        for i in range(len(gas)):
            tot+=gas[i]-cost[i]
            if tot<0:
                tot=0
                ans=i+1
        return ans
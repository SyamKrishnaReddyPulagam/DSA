class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        new={}
        for i in range(n):
            stn="".join(sorted(strs[i]))
            if stn not in new:
                new[stn]=[]
            new[stn].append(strs[i])
        return list(new.values())
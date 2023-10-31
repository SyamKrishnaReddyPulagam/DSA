class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = []
        n = len(pref)
        for i in range(n):
            if i == 0:
                arr.append(pref[i])
                continue
            prev = pref[i - 1]
            curr = pref[i]
            arr.append(prev ^ curr)
        return arr
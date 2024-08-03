class Solution(object):
    def canBeEqual(self, target, arr):
        dicti=Counter(target)
        for i in arr:
            if i in dicti:
                dicti[i]-=1
                if dicti[i]==0:
                    del dicti[i]
            else:
                return False
        if dicti:
            return False
        return True
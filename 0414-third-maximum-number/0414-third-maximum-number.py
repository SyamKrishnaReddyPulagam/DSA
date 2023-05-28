class Solution(object):
    def thirdMax(self, nums):
        res = []
        [res.append(x) for x in nums if x not in res]
        res.sort()
        if(len(res)<3):
            return res[(len(res))-1]
        return res[(len(res))-3]
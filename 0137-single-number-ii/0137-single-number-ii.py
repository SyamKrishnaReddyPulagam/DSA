class Solution(object):
    def singleNumber(self, nums):
        a=[]
        [a.append(i) for i in nums if i not in a]
        b=[]
        for i in a:
            b.append(nums.count(i))
        print(a)
        c=b.index(1)
        return a[c]
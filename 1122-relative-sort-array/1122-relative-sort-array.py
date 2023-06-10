class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        a=[]*len(arr1)
        for i in arr2:
            x=arr1.count(i)
            for j in range(x):
                a.append(i)
        b=[]
        [b.append(i) for i in arr1 if i not in arr2]
        b.sort()
        return a+b
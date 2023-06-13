class Solution(object):
    def findSpecialInteger(self, arr):
        n=len(arr)/4
        c=0
        a=[]
        [a.append(i) for i in arr if i not in a]
        for i in range(len(a)):
            c=0
            for j in range(len(arr)):
                if a[i]==arr[j]:
                    c+=1
            if c>n:
                return a[i]
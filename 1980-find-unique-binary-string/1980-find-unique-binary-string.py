class Solution(object):
    def findDifferentBinaryString(self, nums):
        def recur(n):
            arr=[]
            arr.append("0"*n)
            for i in range(n):
                z=str(bin(2**i).replace("0b",""))
                cache=len(z)
                if cache<n:
                    size=n-cache
                    z="0"*size+z
                arr.append(z)
            return arr
        nums1=recur(len(nums))
        for i in nums1:
            if i not in nums:
                return i
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        nums=[]
        for i in arr:
            z=bin(i).replace("0b","")
            z=z.count("1")
            x=(i,z)
            nums.append(x)
        nums=sorted(nums, key=lambda x: (x[1], x[0]))
        arr=[]
        for i in nums:
            arr.append(i[0])
        return arr
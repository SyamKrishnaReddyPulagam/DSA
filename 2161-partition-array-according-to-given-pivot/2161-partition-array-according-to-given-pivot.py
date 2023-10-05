class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left,equ,right=[],[],[]
        for i in nums:
            if i<pivot:
                left.append(i)
            elif i==pivot:
                equ.append(i)
            else:
                right.append(i)
        return left+equ+right
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n=len(arr)
        if k>=n:
            return max(arr)
        if k==1:
            return max(arr[0],arr[1])
        cur_ele=arr[0]
        cur_ele_rep=0
        for i in range(1,n):
            if arr[i]>cur_ele:
                cur_ele = arr[i]
                cur_ele_rep = 1
            else:
                cur_ele_rep+=1
            if cur_ele_rep==k:
                return cur_ele
        return cur_ele
        
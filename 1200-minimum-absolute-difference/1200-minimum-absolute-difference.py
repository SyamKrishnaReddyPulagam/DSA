class Solution(object):
    def minimumAbsDifference(self, arr):
        min1=10**6
        a=collections.defaultdict(list)
        arr.sort()
        for i in range(len(arr)-1):
            diff=arr[i+1]-arr[i]
            a[diff].append([arr[i],arr[i+1]])
            min1=min(min1,diff)
        return a[min1]
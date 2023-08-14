class Solution(object):
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        print(nums)
        n_largest = heapq.nlargest(k, nums)
        return n_largest[k-1]
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        set1=collections.Counter(arr)
        a=set1.values()
        return len(a)==len(set(a))
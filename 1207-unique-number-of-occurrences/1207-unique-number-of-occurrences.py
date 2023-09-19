class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        set1=collections.Counter(arr)
        a=[]
        for i in set1:
            a.append(set1[i])
        print(a)
        return len(a)==len(set(a))
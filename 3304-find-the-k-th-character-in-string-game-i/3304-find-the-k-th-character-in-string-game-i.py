class Solution:
    def kthCharacter(self, k: int) -> str:
        def func(s):
            ss=""
            for i in s:
                ss+=chr(ord(i)+1)
            return ss
        cur="a"
        while len(cur)<k:
            cur+=func(cur)
        return cur[k-1]
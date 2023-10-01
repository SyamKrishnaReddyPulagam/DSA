class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split(" ")
        for i in range(len(x)):
            x[i]=x[i][::-1]
        return " ".join(x)
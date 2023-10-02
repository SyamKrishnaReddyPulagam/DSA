class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice,bob=0,0
        i=1
        while i<len(colors)-1:
            if colors[i]==colors[i-1] and colors[i]==colors[i+1]:
                if colors[i]=='A':
                    alice+=1
                else:
                    bob+=1
            i+=1
        return alice>bob
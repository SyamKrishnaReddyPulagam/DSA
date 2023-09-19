class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        set1=Counter(word1)
        set2=Counter(word2)
        #return (set1.keys() == set2.keys()) and (set(set1.values())== set(set2.values()))
        
        if (set1.keys() == (set2.keys()) and sorted(set1.values()) == sorted(set2.values())):
            return True
        return False
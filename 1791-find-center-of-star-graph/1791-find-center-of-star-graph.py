class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        temp=edges[0]
        for i in range(1,len(edges)):
            temp=list(set(temp) & set(edges[i]))
        return temp[0]
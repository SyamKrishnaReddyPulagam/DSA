class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dicti={}
        for i in range(len(paths)):
            if paths[i][0] in dicti:
                dicti[paths[i][0]]+=1
            else:
                dicti[paths[i][0]]=1
        for i in range(len(paths)):
            if paths[i][1] not in dicti:
                return paths[i][1]
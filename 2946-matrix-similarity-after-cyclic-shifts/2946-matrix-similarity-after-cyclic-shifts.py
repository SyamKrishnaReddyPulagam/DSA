class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        matrix=mat.copy()
        m,n=len(mat),len(mat[0])
        even,odd=[],[]
        k=k%n
        for i in range(m):
            mat[i]=mat[i][k:]+mat[i][:k]
        return mat==matrix
            
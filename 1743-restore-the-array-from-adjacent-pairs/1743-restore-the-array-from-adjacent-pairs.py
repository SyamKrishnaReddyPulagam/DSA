class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        """n=len(adjacentPairs)
        if n==1:
            return adjacentPairs[0]
        arrlen=(n*2)-2
        #getting the neighbours of each node
        z={}
        for i,j in adjacentPairs:
            if i in z:
                z[i].append(j)
            else:
                z[i]=[j]
            if j in z:
                z[j].append(i)
            else:
                z[j]=[i]
        
        #to get the 0th element of nums check dic with values of length 1
        for i in z:
            if len(z[i])==1:
                start=i
                break
        nums=[]
        nset=set()
        
        while start!=None:
            nums.append(start)
            nset.add(start)
            neigh=z[start]
            start=None
            
            for j in neigh:
                if j not in nset:
                    start=j
        return nums
        """
        
        adjacent = defaultdict(list)
        for u, v in adjacentPairs:
            adjacent[u].append(v)
            adjacent[v].append(u)

        array = []
        for num, neighbours in adjacent.items():
            if len(neighbours) == 1:
                array = [num, neighbours[0]]
                break

        while len(array) < len(adjacentPairs) + 1:
            u, v = adjacent[array[-1]]
            array.append(u if array[-2] == v else v)
        return array
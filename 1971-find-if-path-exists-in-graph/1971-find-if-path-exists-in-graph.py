class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dicti={}
        if not edges or source==destination:
            return True
        for i in range(len(edges)):
            a,b=edges[i]
            if a in dicti:
                dicti[a].append(b)
            else:
                dicti[a]=[b]
            if b in dicti:
                dicti[b].append(a)
            else:
                dicti[b]=[a]
        def bfs(dicti,source,destination):
            queue,visited=deque(),set()
            queue.append(source)
            visited.add(source)
            while queue:
                for i in range(len(queue)):
                    s=queue.popleft()
                    for j in dicti[s]:
                        if j==destination:
                            return True
                        if j not in visited:
                            queue.append(j)
                            visited.add(j)
            return False
        return bfs(dicti,source,destination)
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        def bfs(row,col,img,visited,color):
            visited[row][col]=True
            prev=img[row][col]
            img[row][col]=color
            queue=deque()
            queue.append([row,col])
            while queue:
                for i in range(len(queue)):
                    a,b=queue.popleft()
                    arr=[[a-1,b],[a+1,b],[a,b-1],[a,b+1]]
                    for r,c in arr:
                        if 0<=r<len(img) and 0<=c<len(img[0]) and img[r][c]==prev and not visited[r][c]:
                            visited[r][c]=True
                            img[r][c]=color
                            queue.append([r,c])
            return img
        visited=[[False for _ in range(len(image[0]))] for _ in range(len(image))]
        ans=bfs(sr,sc,image,visited,color)
        return ans
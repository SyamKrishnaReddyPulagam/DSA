class Solution(object):
    def flipAndInvertImage(self, image):
        n=len(image)
        a=0
        b=0
        while a<n:
            while b<n/2:
                temp=image[a][b]
                image[a][b]=image[a][n-1-b]
                image[a][n-1-b]=temp
                b+=1
            b=0
            a+=1 
        i=0
        j=0
        while i<n:
            while j<n:
                if image[i][j]==1:
                    image[i][j]=0
                else:
                    image[i][j]=1
                j+=1
            j=0
            i+=1
        return image
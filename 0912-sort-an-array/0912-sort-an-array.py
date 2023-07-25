class Solution(object):
    def sortArray(self, nums):
        def mergesort(arr,start,end):
            if start>=end:
                return arr
            mid=(start+end)//2
            mergesort(arr,start,mid)
            mergesort(arr,mid+1,end)
            return merge(arr,start,mid,end)
        def merge(array,start,mid,end):
            n1=mid-start+1
            n2=end-mid
            a=[0]*n1
            b=[0]*n2
            for i in range(n1):
                a[i]=array[start+i]
            for i in range(n2):
                b[i]=array[mid+1+i]
            i,j,k=0,0,start
            while i<n1 and j<n2:
                if a[i]<b[j]:
                    array[k]=a[i]
                    i+=1
                else:
                    array[k]=b[j]
                    j+=1
                k+=1
            while i<n1:
                array[k]=a[i]
                i+=1
                k+=1
            while j<n2:
                array[k]=b[j]
                j+=1
                k+=1
            return array
        return mergesort(nums,0,len(nums)-1)
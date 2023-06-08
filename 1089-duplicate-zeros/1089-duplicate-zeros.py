class Solution(object):
    def duplicateZeros(self, arr):
        a=[]
        for i in range(len(arr)):
            if(arr[i]!=0):
                a.append(arr[i]);
            else:
                a.append(arr[i]);
                a.append(0);
        for i in range(len(arr)):
            arr[i]=a[i]
        return arr
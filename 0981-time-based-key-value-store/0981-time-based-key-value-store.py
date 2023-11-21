class TimeMap:

    def __init__(self):
        self.dicti={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dicti:
            self.dicti[key]=[]
        self.dicti[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        z=self.dicti.get(key,[])
        n=len(z)
        l,r=0,n-1
        ans=""
        while l<=r:
            mid=(l+r)//2
            if z[mid][0]<=timestamp:
                ans=z[mid][1]
                l=mid+1
            else:
                r=mid-1
        return ans
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
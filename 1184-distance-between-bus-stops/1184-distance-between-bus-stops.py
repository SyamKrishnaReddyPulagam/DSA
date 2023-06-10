class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        dis1,dis2=0,0
        if start>destination:
            start,destination=destination,start
        for i in range(start,destination,1):
            dis1+=distance[i]
        for j in range(destination,len(distance)):
            dis2+=distance[j]
        for k in range(0,start):
            dis2+=distance[k]
        return min(dis1,dis2)
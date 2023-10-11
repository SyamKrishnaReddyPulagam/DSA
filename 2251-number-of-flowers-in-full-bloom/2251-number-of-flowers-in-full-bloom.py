class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        uniq_people = sorted(list(set(people)))
        ans_map = {}
        flowers.sort()
        f_idx = 0
        cur = []
        heapq.heapify(cur)

        for p in uniq_people:
            # add more flower to the heap if the visit date is greater than flow start date
            while f_idx < len(flowers) and p >= flowers[f_idx][0]:
                # store the end date in the heap
                heapq.heappush(cur, flowers[f_idx][1])
                f_idx += 1
            # remove the flower from the heap if the visit date is greater than flow end date
            while cur and cur[0] < p:
                heapq.heappop(cur)
            
            ans_map[p] = len(cur)

        
        ans = []
        for p in people:
            ans.append(ans_map[p])

        return ans
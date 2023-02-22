class Solution(object):
    def shipWithinDays(self, weights, days):
        maximum_Weight, total_Weight = -1, 0
        for weight in weights:
            maximum_Weight = max(maximum_Weight, weight)
            total_Weight += weight
        i, j = maximum_Weight, total_Weight
        while i < j:
            mid = (i + j) // 2
            days_cal, curr_weight = 1, 0
            for weight in weights:
                if curr_weight + weight > mid:
                    days_cal += 1
                    curr_weight = 0
                curr_weight += weight
            if days_cal > days:
                i = mid + 1
            else:
                j = mid
        return i
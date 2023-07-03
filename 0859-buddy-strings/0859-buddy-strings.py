class Solution(object):
    def buddyStrings(self, s, goal):
        if s == goal and len(s) != len(set(s)):
            return True
        diffs = [i for i in range(len(s)) if s[i] != goal[i]]
        
        return len(s) == len(goal) and len(diffs) == 2 and s[diffs[0]] == goal[diffs[1]] and s[diffs[1]] == goal[diffs[0]]
                    
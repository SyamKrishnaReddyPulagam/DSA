class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        if s==goal:
            return True
        for i in range(1, len(s)):
            ts = s[i:] + s[:i]
            if ts == goal:
                return True
        return False
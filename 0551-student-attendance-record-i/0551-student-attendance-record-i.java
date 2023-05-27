class Solution(object):
    def checkRecord(self, s):
        if(s.count("A")>=2 or s.count("LLL")>0):
            return False
        return True
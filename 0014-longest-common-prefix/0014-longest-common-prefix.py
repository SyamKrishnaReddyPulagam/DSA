class Solution(object):
    def longestCommonPrefix(self, strs):
        x=""
        length=0
        if len(strs)==1:
            return strs[0]
        length = len(strs[0])
        for i in range(1, len(strs)):
            length = min(length, len(strs[i]))
            while length > 0 and strs[0][0:length] != strs[i][0:length]:
                length = length - 1
                if length == 0:
                    return x
        return strs[0][0:length]
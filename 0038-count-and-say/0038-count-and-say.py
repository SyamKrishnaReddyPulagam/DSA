class Solution(object):
    def countAndSay(self, n):
        def cns(str_):
            res = ''
            str_ += '#'
            c = 1
            for i in range(len(str_) - 1):
                if str_[i] == str_[i+1]:
                    c += 1
                    continue
                else:
                    res += str(c) + str_[i]
                    c = 1
            return res
            
        start = "1"
        for i in range(n-1):
            start = cns(start)
        return start
        
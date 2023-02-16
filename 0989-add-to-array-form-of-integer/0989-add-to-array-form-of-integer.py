class Solution(object):
    def addToArrayForm(self, num, k):
        def list_to_array(list1):
            return "".join(map(str,list1))
        a=int(list_to_array(num))
        b=a+k
        res = list(map(int, str(b)))
        return res
class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        s = ''.join(letter for letter in s if letter.isalnum())
        if s==s[::-1]:
            return True
        return False
        
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = []
        total_len = 0

        for char in s:
            if char.isdigit():
                total_len *= int(char)
            else:
                total_len += 1
            stack.append(char)

        while stack:
            char = stack.pop()
            if char.isdigit():
                total_len //= int(char)
                k %= total_len
            else:
                if k == 0 or k == total_len:
                    return char
                total_len -= 1

        return ""
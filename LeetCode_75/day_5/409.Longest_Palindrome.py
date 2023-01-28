class Solution:
    def longestPalindrome(self, s: str) -> int:
        dct = {}
        for item in s:
            if item in dct:
                dct[item] += 1
            else:
                dct[item] = 1

        out = 0
        flag = True
        for value in dct.values():
            if value % 2 == 0:
                out += value
            else:
                out += value if out % 2 == 0 else value - 1

        return out

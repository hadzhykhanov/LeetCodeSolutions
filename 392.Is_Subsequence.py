class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        s_indx = 0

        for item in t:
            if item == s[s_indx]:
                s_indx += 1

            if s_indx >= len(s):
                return True

        return False

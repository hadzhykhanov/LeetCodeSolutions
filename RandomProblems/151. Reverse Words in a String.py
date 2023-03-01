class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(reversed(s.split())))

class Solution:
    def reverseWords(self, s: str) -> str:
        word_starts, word_ends = [], []
        res = []

        if s[0] != " ":
            word_starts.append(0)

        for i in range(1, len(s)):
            if s[i] != " " and s[i - 1] == " ":
                word_starts.append(i)

            if s[i] == " " and s[i - 1] != " ":
                word_ends.append(i)

        if s[len(s) - 1] != " ":
            word_ends.append(len(s))

        for start, end in zip(word_starts, word_ends):
            res.append(s[start:end])

        return " ".join(list(reversed(res)))
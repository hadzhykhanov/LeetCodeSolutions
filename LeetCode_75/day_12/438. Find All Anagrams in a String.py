class Solution:
    @staticmethod
    def make_dict_from_str(p):
        dct = {}
        for item in p:
            if item in dct:
                dct[item] += 1
            else:
                dct[item] = 1

        return dct

    @staticmethod
    def get_history(s, p):
        history = {}
        for i in range(len(p)):
            if s[i] in history:
                history[s[i]] += 1
            else:
                history[s[i]] = 1

        return history

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []

        answer = []
        p_dict = self.make_dict_from_str(p)
        history = self.get_history(s, p)

        first, second = 0, len(p) - 1

        while second != len(s):
            if p_dict == history:
                answer.append(first)

            history[s[first]] -= 1
            if history[s[first]] == 0: history.pop(s[first])

            first, second = first + 1, second + 1

            if second != len(s):
                if s[second] in history:
                    history[s[second]] += 1
                else:
                    history[s[second]] = 1

        return answer


class Solution:
    @staticmethod
    def make_dict_from_str(p):
        dct = {}
        for item in p:
            if item in dct:
                dct[item] += 1
            else:
                dct[item] = 1

        return dct

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []

        answer = []
        p_dict = self.make_dict_from_str(p)
        memory = dict()

        left = 0

        for right in range(len(s)):
            if s[right] in memory:
                memory[s[right]] += 1
            else:
                memory[s[right]] = 1

            if right - left == len(p):
                memory[s[left]] -= 1
                if memory[s[left]] == 0: memory.pop(s[left])

                left += 1

            if memory == p_dict:
                answer.append(left)

        return answer



















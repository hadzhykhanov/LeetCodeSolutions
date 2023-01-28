class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct = dict()
        for i, item in enumerate(s):
            if item not in dct:
                dct[item] = set()
            dct[item].add(t[i])

        global_set = set()
        global_len = 0
        for value in dct.values():
            global_set.update(value)
            global_len += len(value)

        if len(global_set) != global_len:
            return False

        for value in dct.values():
            if len(value) >= 2:
                return False

        return True

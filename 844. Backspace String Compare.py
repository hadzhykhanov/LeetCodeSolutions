class Solution:
    @staticmethod
    def get_processed_string(string):
        stack = []
        for item in string:
            if item != "#":
                stack.append(item)
            elif stack:
                stack.pop()

        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        if self.get_processed_string(s) == self.get_processed_string(t):
            return True

        return False


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_idx, t_idx = len(s) - 1, len(t) - 1
        s_counter, t_counter = 0, 0

        while s_idx >= 0:
            if s[s_idx] == "#":
                s_counter += 1

            elif s_counter > 0:
                s_counter -= 1

            else:
                while t_idx >= 0:
                    if t[t_idx] == "#":
                        t_counter += 1

                    elif t_counter > 0:
                        t_counter -= 1

                    elif s[s_idx] == t[t_idx]:
                        t_idx -= 1
                        break

                    t_idx -= 1

                else:
                    return False

            s_idx -= 1

        while t_idx >= 0:
            if t[t_idx] == "#":
                t_counter += 1

            elif t_counter > 0:
                t_counter -= 1

            else:
                return False

            t_idx -= 1

        return True


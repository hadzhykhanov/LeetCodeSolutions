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

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for idx, item in enumerate(s):
            if item != "]":
                stack.append(item)
            else:
                curr_popped = stack.pop()
                curr_elements = [curr_popped]
                curr_digits = []

                while curr_elements[-1] != "[":
                    curr_popped = stack.pop()
                    curr_elements.append(curr_popped)
                else:
                    curr_elements.pop()
                    while stack and stack[-1].isdigit():
                        curr_digit = stack.pop()
                        curr_digits.append(curr_digit)

                curr_elements.reverse()
                curr_digits.reverse()
                curr_st, curr_multiplier = "".join(curr_elements), int("".join(curr_digits))

                stack.append(curr_multiplier * curr_st)

        return "".join(stack)


s = Solution()
print(s.decodeString("3[a2[c]b]"))

class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        cur_char = chars[left]
        counter = 1

        chars.append(None)

        for right in range(1, len(chars)):
            if chars[right] != cur_char:
                chars[left] = cur_char
                left += 1

                if counter != 1:
                    for digit in str(counter):
                        chars[left] = digit
                        left += 1

                cur_char = chars[right]
                counter = 1

            else:
                counter += 1

        for _ in range(len(chars) - left):
            chars.pop()


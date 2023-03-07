class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        target = chr(ord(target) + 1)

        while left <= right:
            middle = (left + right) // 2
            if letters[middle] == target:
                return target
            elif letters[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return letters[left] if left != len(letters) else letters[0]

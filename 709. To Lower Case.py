class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join([chr(ord(item) + 32) if "A" <= item <= "Z" else item for item in s])

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum()).lower()

        if clean == clean[::-1]:
            return True
        else:
            return False
        
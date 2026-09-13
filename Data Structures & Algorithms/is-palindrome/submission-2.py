class Solution:
    def isPalindrome(self, s: str) -> bool:
        nonSpaces = "".join(c for c in s if c.isalnum())
        left = 0
        right = len(nonSpaces) - 1
        while left < right:
            
            if nonSpaces[left].lower() != nonSpaces[right].lower():

                return False

            left += 1
            right -= 1

        return True

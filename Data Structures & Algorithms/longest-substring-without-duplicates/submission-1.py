class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        subString = set()
        left = 0
        result = 0

        for r in range(len(s)):
            while s[r] in subString:
                subString.remove(s[left])
                left += 1
            subString.add(s[r])

            result = max(result, r - left + 1)
                
        return result 
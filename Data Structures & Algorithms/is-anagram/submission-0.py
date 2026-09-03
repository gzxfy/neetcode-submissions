class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstString = {}
        secondString = {}

        for i in range(len(s)):
            if s[i] not in firstString:
                firstString[s[i]] = 1
            else:
                firstString[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in secondString:
                secondString[t[i]] = 1
            else:
                secondString[t[i]] += 1

        return firstString == secondString
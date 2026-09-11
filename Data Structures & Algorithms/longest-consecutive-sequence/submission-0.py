class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nonDupe = set(nums)

        for i in nums:
            if (i - 1) not in nonDupe:
                length = 0
                while (i + length) in nonDupe:
                    length += 1
                longest = max(length, longest)

        return longest
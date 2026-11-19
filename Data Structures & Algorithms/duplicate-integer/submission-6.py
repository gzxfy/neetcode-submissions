class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nonDupe = set(nums)
        if len(nonDupe) == len(nums):
            return False
        else:
            return True
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        for i in count:
            if count[i] >= 2:
                return True

        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        result = False
        for i in nums:
            if i not in count:
                count[i] = 0
            else: 
                return True
        return result

        
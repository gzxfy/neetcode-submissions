class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        holder = {}

        for i in nums:
            if i not in holder:
                holder[i] = i
            else:
                return True

        return False
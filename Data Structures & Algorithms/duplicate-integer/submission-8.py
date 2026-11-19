class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        holder = {}
        for i in range(len(nums)):
            if nums[i] not in holder:
                holder[nums[i]] = i
            else:
                return True

        
        return False
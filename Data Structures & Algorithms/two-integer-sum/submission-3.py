class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for index, i in enumerate(nums):
            search = target - i
            if search in count:
                return [count[search], index]
            count[i] = index
        
        
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in count:
                return [count[remainder], i]

            count[nums[i]] = i;
     
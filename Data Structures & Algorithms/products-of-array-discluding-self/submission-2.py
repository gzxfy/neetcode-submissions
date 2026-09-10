class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            # print(f"This is iteration {i}. The array is {result} and the prefix is {prefix}")
            result[i] = prefix
            prefix *= nums[i]
        # print(f"this is the array at the end {result}")
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
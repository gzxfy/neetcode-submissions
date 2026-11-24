class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sortedNums = sorted(nums)

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
        
            while left < right:
                holder = sortedNums[i] + sortedNums[left] + sortedNums[right]

                if holder == 0 and [sortedNums[i], sortedNums[left], sortedNums[right]] not in result:
                    result.append([sortedNums[i], sortedNums[left], sortedNums[right]])
                elif holder < 0:
                    left += 1
                else:
                    right -= 1
                    
                
        

        return result



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) < k:
            return []

        result = {}

        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1


        sorted_keys = sorted(result, key=lambda x: result[x], reverse=True)
        return sorted_keys[:k]
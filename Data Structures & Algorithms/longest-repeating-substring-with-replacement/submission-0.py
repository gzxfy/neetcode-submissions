class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        counts = {}
        max_frequency = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1

            max_frequency = max(max_frequency, counts[s[right]])

            window_size = right - left + 1

            while window_size - max_frequency > k:
                counts[s[left]] -= 1
                left += 1
                window_size = right - left + 1

            result = max(result, window_size)

        return result
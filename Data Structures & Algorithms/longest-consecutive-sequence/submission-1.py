class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0

        for n in nums:
            length = 0
            if (n-1) not in numSet:
                while (n + length) in numSet:
                    length += 1
            ans = max(ans, length)

        return ans
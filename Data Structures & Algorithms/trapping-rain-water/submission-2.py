class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        for i in range(0,n-1):
            prefix[i+1] = max(prefix[i], height[i])

        for i in range(n-1,0,-1):
            suffix[i-1] = max(suffix[i], height[i])

        ans = 0

        for i in range(0,n):
            ans += max(min(prefix[i],suffix[i]) - height[i],0)

        return ans
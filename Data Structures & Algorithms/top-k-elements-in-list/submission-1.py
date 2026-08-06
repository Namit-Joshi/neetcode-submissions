from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)

        for num in nums:
            store[num] += 1

        vals = sorted(store.values(), reverse=True)
        freq = []

        for i in range(k):
            freq.append(vals[i])

        ans = []
        for key, value in store.items():
            if value in freq:
                ans.append(key)

        return ans

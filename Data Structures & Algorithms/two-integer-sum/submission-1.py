class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {} # val -> index
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in store:
                return [store[diff], idx]
            store[num] = idx
            
        
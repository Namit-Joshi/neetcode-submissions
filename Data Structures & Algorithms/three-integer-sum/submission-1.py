class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        for i in range(0,len(nums)):
            l, r = i + 1, len(nums) - 1

            req_sum = 0 - nums[i]

            while(l < r):
                if nums[l] + nums[r] > req_sum:
                    r -= 1
                elif nums[l] + nums[r] < req_sum:
                    l += 1
                else:
                    triplet = [nums[i], nums[l], nums[r]]
                    if triplet not in ans:
                        ans.append(triplet)
                    l += 1
                    r -= 1
        return ans

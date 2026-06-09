class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        result = []
        for i in range(len(nums)):
            if (target - nums[i]) in sums:
                result.append(min(sums[target - nums[i]], i))
                result.append(max(sums[target - nums[i]], i))
            else:
                sums[nums[i]] = i
        return result

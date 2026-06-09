class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_check = {}
        # for item in nums:
        #     if item not in nums_check:
        #         nums_check[item] = 1
        #     else:
        #         nums_check[item] += 1
        # for key in nums_check:
        #     if nums_check[key] > 1:
        #         return True
        # return False
        nums_check = set(nums)
        if len(nums) != len(nums_check):
            return True
        return False

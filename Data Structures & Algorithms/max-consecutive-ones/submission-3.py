class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = current_streak = 0
        for num in nums:
            if num == 1:
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 0
        return max(max_streak, current_streak)
            
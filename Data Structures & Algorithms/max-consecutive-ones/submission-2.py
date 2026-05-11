class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        current_streak = 0
        for num in nums:
            print(num, current_streak)
            if num == 1:
                current_streak += 1
            else:
                if current_streak > max_streak:
                    max_streak = current_streak
                current_streak = 0
        if current_streak > max_streak:
            max_streak = current_streak
        return max_streak
            
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1=0
        count_1=0
        i=0
        while i<len(nums):
            if nums[i] == 1:
                count_1 += 1
                max_1 = max(max_1, count_1)
            else:
                count_1 = 0
            i += 1
        return max_1

        
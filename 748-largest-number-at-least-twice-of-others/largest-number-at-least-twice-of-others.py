class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x=sorted(nums)[-1]
        y=sorted(nums)[-2]
        if x>=(2*y):
            return nums.index(x)
        return -1
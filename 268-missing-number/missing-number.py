class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for x in range(n+1):
            if nums.count(x)==0:
                return x
        
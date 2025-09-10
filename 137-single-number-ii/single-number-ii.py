class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=Counter(nums)
        for num in nums:
            if x[num]==1:
                return num
        
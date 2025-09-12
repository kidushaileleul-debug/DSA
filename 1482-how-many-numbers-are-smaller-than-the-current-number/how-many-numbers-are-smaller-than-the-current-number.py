class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x=sorted(nums)
        y=[]
        for num in nums:
            y.append(x.index(num))
        return y
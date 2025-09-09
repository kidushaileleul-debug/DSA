class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x=sorted(set(nums))
        if len(x)<3:
            return x[-1]
        else:
            return x[-3]

        
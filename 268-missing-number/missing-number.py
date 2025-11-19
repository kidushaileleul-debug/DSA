class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=set()
        for i in range(len(nums)+1):
            x.add(i)
        y=x-set(nums)
        return y.pop()
        
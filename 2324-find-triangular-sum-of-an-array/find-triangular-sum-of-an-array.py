class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            x=[]
            for i in range(len(nums)-1):
                p=(nums[i]+nums[i+1])%10
                x.append(p)
            nums=x
        return nums[0]
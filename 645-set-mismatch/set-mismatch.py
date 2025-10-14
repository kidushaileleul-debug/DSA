class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x=Counter(nums)
        duplicate=None
        for i in range(len(nums)):
            if x[nums[i]]==2:
                duplicate=nums[i]
                break
        for i in range(1,len(nums)+1):
            if i not in x:
                return [duplicate,i]
            


    
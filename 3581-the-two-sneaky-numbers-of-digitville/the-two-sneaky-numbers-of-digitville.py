class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        x=[]
        for i in range(len(nums)):
            if nums.count(i)>1:
                x.append(i)
            if len(x)==2:
                break 
        return x
        
        
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        x=Counter(nums)
        y=[]
        for num in x:
            if x[num]>n//3:
                y.append(num)
        return y


        
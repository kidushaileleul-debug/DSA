class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        if n<k:
            return None
        x=sum(nums[:k])
        y=x
        for i in range(k,n):
            x+=nums[i]-nums[i-k]
            y=max(x,y)
        return y/k
        
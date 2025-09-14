class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        x=0
        while l<r:
            if nums[l]+nums[r]==k:
                x+=1
                l+=1
                r-=1
            elif nums[l]+nums[r]<k:
                l+=1
            else:
                r-=1
        return x

        
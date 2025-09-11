class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_seq =1
        count_seq =1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count_seq+=1
                max_seq=max(max_seq,count_seq)
            else:
                count_seq=1
        return max_seq

        
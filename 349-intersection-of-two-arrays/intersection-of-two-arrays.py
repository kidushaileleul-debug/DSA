class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = []
        nums2=set(nums2)
        for i in set(nums1):
            if i in nums2:
                x.append(i)
        return x


        
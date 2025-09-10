class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = []
        nums2_copy = nums2.copy()
        for num in nums1:
            if num in nums2_copy:
                x.append(num)
                nums2_copy.remove(num)
        return x

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x=len(nums)
        z=set(nums)
        y=[]
        for i in range(1,x+1):
            if i not in z:
                y.append(i)
        return y

        
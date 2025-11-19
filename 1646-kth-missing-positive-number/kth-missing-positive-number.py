class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        x=arr[-1]+k
        y=[]
        for i in range(1,x+1):
            if i not in arr:
                y.append(i)
        return y[k-1]
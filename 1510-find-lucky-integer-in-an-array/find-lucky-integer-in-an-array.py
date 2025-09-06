class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x=[]
        for i in arr:
            if i==arr.count(i):
                x.append(i)
        if len(x)>0:
            return max(x)
        else:
            return -1
        
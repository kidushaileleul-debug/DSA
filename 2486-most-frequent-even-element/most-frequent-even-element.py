class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        x=Counter(nums)
        values = []
        for n in x:
            if n%2==0:
                values.append(x[n])
        if not values:
            return -1
        y=[]
        for num in x:
            if x[num]==max(values) and num%2==0:
                y.append(num)
        return min(y)
        
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=float("inf")
        x=0
        for price in prices:
            minn=min(price,minn)
            x=max(x,price-minn)
        if x>0:
            return x
        return 0
            
            
        
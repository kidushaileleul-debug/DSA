class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x=[]
        for num in str(n):
            x.append(int(num))
        n_sum=sum(x)
        n_product=1
        for i in x:
            n_product*=i
        return n_product-n_sum
        
        
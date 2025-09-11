class Solution:
    def sumZero(self, n: int) -> List[int]:
        x=[]
        for i in range(1,n//2+1):
            x.append(-i)
            x.append(i)
        if n%2==1:
            x.append(0)
        return x
            
        
        
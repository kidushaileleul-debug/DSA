class Solution:
    def selfDividingNumbers(self,left:int,right:int)->List[int]:
        x=[]
        for i in range(left,right+1):
            if all(int(y)!=0 and i%int(y)==0 for y in str(i)):x.append(i)
        return x

        
            
        
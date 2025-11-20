class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        x=[]
        for i in range(len(l)):
            y=nums[l[i]:r[i]+1]
            if len(y)<=2:
                x.append(True)
                continue
            y=sorted(y)
            p=y[1]-y[0]
            T=True
            for j in range(1,len(y)):
                if y[j]-y[j-1]!=p:
                    T=False
                    break
            x.append(T)
        return x
                

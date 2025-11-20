class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        x=[]
        for i in range(numRows):
            y=[1]*(i+1)
            for j in range(1,i):
                y[j]=x[i-1][j-1]+x[i-1][j]
            x.append(y)
        return x
        
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]=digits[-1]+1
            return digits
        else:
            x=""
            for i in digits:
                x+=str(i)
            s=str(int(x)+1)
            y=[]
            for char in s:
                y.append(int(char))
            return y

        
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>1:
            y=[]
            for i in range(len(str(num))):
                y.append(int(str(num)[i]))
            num=sum(y)
        return num


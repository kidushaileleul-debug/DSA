class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        y=""
        c=""
        for num in x:
            if num=="-":
                y+="-"
            else:
                c+=num
        d=c[::-1]
        answer=int(y+d)
        if answer < -2**31 or answer > 2**31 - 1:
            return 0
        return answer
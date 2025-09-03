class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        x = 0
        while 2**x <= n:
            if n%2!=0 and n!=1:
                return False
            elif 2**x == n:
                return True
            x += 1
        return False


        
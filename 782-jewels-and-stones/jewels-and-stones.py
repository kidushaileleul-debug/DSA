class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x=0
        for j in jewels:
            x+=stones.count(j)
        return x
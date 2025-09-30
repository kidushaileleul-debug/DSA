class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x=Counter(stones)
        y=0
        for i in range(len(jewels)):
            if jewels[i] in stones:
                y+=x[jewels[i]]
        return y
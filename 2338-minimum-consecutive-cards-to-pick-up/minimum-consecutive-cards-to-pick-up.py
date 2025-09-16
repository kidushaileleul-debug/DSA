class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        x=set()
        l=0
        y=float('inf')
        for r in range(len(cards)):
            while cards[r] in x:
                y=min(y,r-l+1)
                x.remove(cards[l])
                l+=1
            x.add(cards[r])
        return y if y!=float('inf') else -1
        
class Solution:
    def checkRecord(self, s: str) -> bool:
        x=Counter(s)
        if x["A"]<2 and "LLL" not in s:
            return True
        return False
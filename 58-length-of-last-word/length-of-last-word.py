class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=s.split()[-1]
        return len(x)
        
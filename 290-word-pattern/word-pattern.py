class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(s.split(" "))!=len(pattern):
            return False
        elif len(set(pattern))==len(set(s.split(" "))):
            return all(pattern.index(c)==s.split(" ").index(w) for c, w in zip(pattern,s.split(" ")))
        else:
            return False
        
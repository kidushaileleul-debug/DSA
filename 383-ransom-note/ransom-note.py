class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x=Counter(ransomNote)
        y=Counter(magazine)
        for i in range(len(ransomNote)):
            if y[ransomNote[i]]<x[ransomNote[i]]:
                return False
        return True
        
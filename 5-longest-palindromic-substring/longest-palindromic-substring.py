class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=""
        for r in range(len(s)):
            l=0
            while l<=r:
                x=s[l:r+1]
                if x==x[::-1] and len(x)>len(longest):
                    longest=x
                l+=1
        return longest

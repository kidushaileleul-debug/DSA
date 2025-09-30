class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx=0
        l=0
        y=set()
        for i in range(len(s)):
            while s[i] in y:
                y.remove(s[l])
                l+=1
            y.add(s[i])
            maxx=max(maxx,i-l+1)
        return maxx
        
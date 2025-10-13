class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<k:
            return s[::-1]   
        if len(s)>k and len(s) < 2*k:
            return s[:k][::-1]+s[k:]
        else:
            l=0
            r=k
            s=list(s)
            while l<len(s):
                s[l:r]=s[l:r][::-1]
                l+=2*k
                r=l+k
        return "".join(s)

        
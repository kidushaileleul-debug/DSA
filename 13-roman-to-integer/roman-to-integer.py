class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
                    }
        l=0
        x=0
        while l<len(s):
            if l + 1 < len(s) and dic[s[l]]<dic[s[l+1]]:
                y=dic[s[l+1]]-dic[s[l]]
                x+=y
                l+=2
            else:
                x+=dic[s[l]]
                l+=1
        return x
        
        
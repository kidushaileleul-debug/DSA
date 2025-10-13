class Solution:
    def reverseVowels(self, s: str) -> str:
        x=set("aeiouAEIOU")
        y=[]
        for char in s:
            y.append(char)
        r=len(s)-1
        for i in range(len(y)):
            if i>=r:
                break
            while r>i and y[r].lower() not in x:
                r-=1
            if y[i].lower() in x:
                y[i],y[r]=y[r],y[i]
                r-=1
        return "".join(y)

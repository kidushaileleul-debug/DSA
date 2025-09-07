class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        x=[]
        for y in zip(*strs):
            x.append(y)
        z=[]
        for i in x:
            if len(set(i))==1:
                z.append(i[0])
            else:
                break
        return "".join(z)
        
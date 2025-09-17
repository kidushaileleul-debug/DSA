class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l=0
        r=len(skill)-1
        x=[]
        target=skill[l]+skill[r]
        while l<r:
            if skill[l]+skill[r]!=target:
                return -1
            x.append([skill[l],skill[r]])
            l+=1
            r-=1
        y=0
        for i in x:
            y+=i[0]*i[1]
        return y

            

        
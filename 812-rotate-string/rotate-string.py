class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
       count=0
       s=list(s)
       goal=list(goal)
       while count<len(s):
        item=s.pop(0)
        s.append(item)
        if s==goal:
            return True
        count+=1
       return False


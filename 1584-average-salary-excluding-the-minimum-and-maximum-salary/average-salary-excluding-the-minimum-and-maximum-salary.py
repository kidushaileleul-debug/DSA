class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n=len(salary)-2
        x=sum(salary)-(salary[0]+salary[-1])
        average=x/n
        return average
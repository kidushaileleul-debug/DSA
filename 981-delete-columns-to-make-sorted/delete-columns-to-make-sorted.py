class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for x in zip(*strs):
            if list(x)!=sorted(list(x)):
                count+=1
        return count
        
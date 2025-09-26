class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_copy=score.copy()
        sorted_scores=sorted(score_copy,reverse=True)
        max1=sorted_scores[0] if len(sorted_scores)>0 else None
        max2=sorted_scores[1] if len(sorted_scores)>1 else None
        max3=sorted_scores[2] if len(sorted_scores)>2 else None
        x=sorted(score,reverse=True)
        for i in range(len(score)):
            if score[i]==max1:
                score[i]="Gold Medal"
            elif score[i]==max2:
                score[i]="Silver Medal"
            elif score[i]==max3:
                score[i]="Bronze Medal"
            else:
                score[i]=str(x.index(score[i])+1)
        return score

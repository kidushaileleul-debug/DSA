class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxx=0
        while i<j:
            x=min(height[i],height[j])
            maxx=max(maxx,x*(j-i))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxx

        
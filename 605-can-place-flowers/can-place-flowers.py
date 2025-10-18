class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        count=0
        length=len(flowerbed)
        if length==1:
            return n<=1 and flowerbed[0]==0
        if flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0]=1
            count+=1
        for i in range(1,length-1):
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                count+=1
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            flowerbed[-1]=1
            count+=1
        return count>=n


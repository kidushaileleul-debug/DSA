class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        x=[]
        for i in range(1,n+1):
            x.append(str(i))
        for j in range(n):
            if int(x[j])%5==0 and int(x[j])%3==0:
                x[j]="FizzBuzz"
            elif int(x[j])%3==0:
                x[j]="Fizz"
            elif int(x[j])%5==0:
                x[j]="Buzz"
        return x
                
                    
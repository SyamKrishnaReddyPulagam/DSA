class Solution(object):
    def fizzBuzz(self, n):
        answer=[]
        for i in range(n):
            answer.append(str(i+1))
        for i in range(2,n,3):
            answer[i]="Fizz"
        for i in range(4,n,5):
            answer[i]="Buzz"
        for i in range(14,n,15):
            answer[i]="FizzBuzz"
        return answer
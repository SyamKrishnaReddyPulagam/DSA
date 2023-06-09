class Solution(object):
    def multiply(self, num1, num2):
        num2=num2[::-1]
        b=1
        c=pow(10,len(num1)-1)
        x,y=0,0
        for i in num2:
            a=c
            x=0
            for j in num1:
                x+=int(i)*int(j)*a
                a=a/10
            y+=x*b
            b=b*10
        return str(y)
                
                
                
        
#python program to check given number is neon or not
n=int(input("enter an integer number"))
sq=n*n
sum=0
temp=n

while sq!=0:
    r=sq%10
    sum=sum+r
    sq=sq//10

if n==sum:
    print(n,"is neon number")
else:
    print(n,"is not a neon number")

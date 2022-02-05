a=int(input("enter number"))
def sum():
    i=0
    sum=0
    while i<=a:
        if i%3==0 or i%5==0:
            print(i)
            sum+=i
        i+=1
    print(sum)
sum()
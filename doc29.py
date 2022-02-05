def sum():
    a=int(input("enter number"))
    i=0
    s=0
    while i<=a:
        if i%3==0 or i%5==0:
            s+=i
        i+=1
    print(s)
sum()
             
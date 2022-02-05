def prime():
    a=int(input("enter number"))
    i=1
    f=0
    while i<=a:
        if a%i==0:
            f+=1
        i+=1
    if f==2:
        print(a,"prime number")
    else:
        print(a,"not prime number")
prime()
        
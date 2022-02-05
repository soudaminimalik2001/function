user=int(input("enter number"))
def a(user):
    i=1
    sum=0
    while i<user:
        if user%i==0:
            sum+=i
        i+=1
    if sum==user:
        print(user,"perfect number")
    else:
        print(user,"not perfect number")
a(user)
    
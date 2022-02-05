def sum(*a):
    i=0
    s=0
    while i<len(a):
        s=s+a[i]
        print(s)
        i+=1
sum(5,7,3)
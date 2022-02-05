def sum(*a):
    i=0
    s=0
    while i<len(a):
        c=s+a[i]
        print(c)
        i+=1
sum(5,7,3)
#arbitrary positional argument   
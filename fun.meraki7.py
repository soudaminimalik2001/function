def a():
    b=["hello","welcome"]
    i=0
    while i<len(b):
        if len(b[0])==len(b[1]):
            print(b[i],end=" ")
        elif len(b[0])!=len(b[1]):
            print(b[i])
        i+=1
a()

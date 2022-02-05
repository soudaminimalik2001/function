def a():
    b="The quick Brow Fox"
    i=0
    c=0
    c1=0
    while i<len(b):
        if b[i]>"a" and b[i]<"z":
            c+=1
        elif b[i]>"A" and b[i]<"Z":
            c1+=1
        i+=1
    print("uppercase",c1)
    print("lowercase",c)
a()
        
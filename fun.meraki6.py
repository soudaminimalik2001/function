user=int(input("enter speed"))
def speed():
    i=0
    c=0
    while i>0:
        if i<70:
            print("ok")
        if i>70:
            if i%5==0:
                c+=1
        i+=1
    if c>12:
        print("license suspand")
speed()
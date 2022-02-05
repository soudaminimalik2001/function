def shownumber():
    a=int(input("enter number:"))
    i=0
    while i<=a:
        if i%2==0:
            print(i,"even")
        elif i%2!=0:
            print(i,"odd")
        i+=1
shownumber()
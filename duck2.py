def max():
    a=int(input("enter 1st number"))
    b=int(input("enter 2nd number"))
    c=int(input("enter 3rd number"))
    if a<b>c:
        print(b,"maximum")
    elif a<c>b:
        print(c,"maximum")
    else:
        print(a,"maximum")
max()
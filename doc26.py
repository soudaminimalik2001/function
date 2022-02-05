def func():
    a=int(input("enter number"))
    if a%3==0:
        print("fizz")
    elif a%5==0:
        print("buzz")
    elif a%3==0 and a%5==0:
        print("fizzbuzz")
    else:
        print(a)
func()
    
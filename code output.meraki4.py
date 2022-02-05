def sumofdigits(number):
    sum = 0
    i=0
    modulus = 0
    while number>i:
        modulus = number%10
        sum+=modulus
        number/=10
        i+=1
        print(sum)
sumofdigits(123)
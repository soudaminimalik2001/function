def prime():
    a=int(input("enter number:"))
    i=1
    while i<=a:
	    j=1
	    f=0
	    while j<=i:
		    if i%j==0:
			    f+=1
		    j+=1
	    if f==2:
		    print(i,'prime number')
	    else:
		    print(i)
	    i+=1
prime()
#1 to 50 prime number
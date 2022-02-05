list1=[2,-7,5,-64,-14]
def num():
    i=0
    c=0
    c1=0
    while i<len(list1):
        if list1[i]<0:
            c+=1
        else:
            c1+=1
        i+=1
    print('neg','=',c)
    print('pos','=',c1)
num()
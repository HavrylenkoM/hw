a = int(input())
b = int(input())
c = int(input())



for i in range(1, c+1): 
    if i % a == 0:
        print ('F')
    elif i % b == 0:
        print ('B')
    elif i % a == 0 and i % b == 0:
        print ('FB')
    else:
        print (i)

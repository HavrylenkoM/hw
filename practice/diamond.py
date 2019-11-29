x = int(input())

if x <= 0 :
    print("error")
elif x % 2 == 0:
    print('error')
elif x == 1 :
    print("*")
elif x == 3 :
    print(' * ')
    print('***')
    print(' * ')
elif x == 5 :
    print('  *  ')
    print(' *** ')
    print('*****')
    print(' *** ')
    print('  *  ')
else:
    print('error')


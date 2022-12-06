mail=lambda a,b:(a-b)+b
while True:
    a=input('Enter a valid e-mail adress:-')
    if '@' in a:
        a=a.split('@')
        print('Username:- {} and Domain:- {}'.format(a[0],a[1])) #print
    else:
        print('E-mail is not Valid')

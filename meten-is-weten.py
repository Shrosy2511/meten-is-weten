a = int(input('a vul een geheel getal in '))
b = int(input('b vul een geheel getal in '))
min = b
max = a

if a > b:
    print('het maximun is: ' + str(max))
elif a < b:
    print('het minimum is: ' + str(max))

if b > a:
    print('het maximum is: ' + str(min))
elif b < a:
    print('het minimum is: '+ str(min))
else:
    print('a en b zijn even groot')
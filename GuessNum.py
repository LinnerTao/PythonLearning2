import random
s=int(random.uniform(1,10))
m=int(input('Please Input Num:'))
while m!=s:
    if m>s:
        print('Bigger')
        m=int(input("Please Input Num:"))

    if m<s:
        print('Smaller')
        m=int(input('Please Input Num:'))
    if m==s:
        print('ok')
        break
from random import randint
x=1
while True:
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    if d1 != d2:
        print(d1,d2)
    elif d1 == d2:
        print(d1,d2)
        break
    print(x,"vezes.")
    x= x+1
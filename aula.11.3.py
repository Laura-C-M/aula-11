from random import randint
print("Este código vais escolher um nº de 0 a 5")
n = randint(0,5)
while True:
    nu = int(input("Que número achas que é?"))
    if n != nu:
        print("Estás errado tenta novamente!")
    elif n == nu:
        print("Estás certo parabéns!")
        break
import random

print("\tПеред вами симулятор бросания монетки 100 раз подряд\n")

#орел
side1 = 0
#решка
side2 = 0

for i in range(100):
    i = random.randint(0,1)
    if i == 0:
        side1 += 1
    else:
        side2 += 1

print("\n\nЯ сто раз подбросил монетку и вот, что у меня вышло: ", side1, "орлов", side2, "решек\n")
input("\n\nНажмите Enter, чтобы выйти.")

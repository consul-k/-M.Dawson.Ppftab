import random

print("\tПеред вами симулятор бросания монетки 100 раз подряд\n")
side1 = random.randint(1, 100)
side2 = 100 - side1
print("\n\nЯ сто раз подбросил монетку и вот, что у меня вышло: ", side1, "орлов", side2, "решек\n")
input("\n\nНажмите Enter, чтобы выйти.")

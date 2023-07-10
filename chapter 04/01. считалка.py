print("\tПосчитаем:\n")

a = int(input("Введите начало счета: "))
b = int(input("Введите конец света: "))    
c = int(input("Введите интервал: "))
for i in range(a,b,c):
        print(i, end=" ")
input("\n\nНажмите Enter, чтобы выйти.\n")

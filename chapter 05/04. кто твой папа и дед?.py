'''

Доработайте программу «Кто твой папа?» так, чтобы можно было, введя имя человека, узнать, кто его дед.
Программа должна по-прежнему пользоваться одним словарем с парами «сын - отец». Подумайте, как
включить в этот словарь несколько поколений.

'''

son_dad = {'Tirion' : {'father':'Taiwin','grandpa':'Some Targarien!'},
           'Aria' : {'father': 'Ned Star','grandpa':'Some sad Stark'},
           'Jon' : {'father': 'Raegar','grandpa': 'Mad Targarien king'},
           'Jendry' : {'father':'Robert','grandpa': 'Who if not the Targarien?'}}

choice = None

while choice != "0":
    print(
    """
    Управление программой:
    0 - Выйти
    1 - Найти отца персонажа
    2 - Добавить пару
    3 - Изменить отца
    4 - Удалить пару
    5 - Экслюзивная функция, узнай деда персонажа
    """
    )
    choice = input("Ваш выбор: ")

    print()     #?
    if choice == "0":
        print("До свидания")
    elif choice == "1":
        son = input("Чей отец вам интересен? ")
        if son in son_dad:
            father = son_dad[son]
            print("\n", son,"имеет отца",father)
        else:
            print("\nУвы, нет данных о: ", son)
    elif choice == "2":
        son = input("Какого отпрыска вы хотите добавить? ")
        if son not in son_dad:
            father = input("\nВведите отца: ")
            son_dad[son] = father
            print("\nГерой", son, "добавлен в словарь.")
        else:
            print("\nТакой герой уже есть!")
    elif choice == "3":
        son = input("Чьего отца вы хотите изменить? ")
        if son in son_dad:
            father = input("Введите нового отца: ")
            son_dad[son] = father
            print("\nГерой", son, "получил исправленную версию!")
        else:
            print("\nТакого героя у нас нет!")
    elif choice == "4":
        son = input("Какого героя вы хотите удалить? ")
        if son in son_dad:
            del son_dad[son]
            print("\nГерой", son, "удален.")
    elif choice == "5":
        son = input("Назовите того, чьей дед вам интересен! ")
        if son in son_dad:
            grandpa = son_dad[son]['grandpa']
            print("\n", son,"был бы не им, если бы не дед: ",grandpa)  
        else:
            print("\nНичем не могу помочь. Героя ",son,"нет в словаре")

    else:
        print("В меня нет такого пункта", choice)
        
    input("\n\nНажмите Enter, чтобы выйти.")

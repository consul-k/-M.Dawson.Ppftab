'''

Напишите программу «Кто твой папа?», в которой пользователь будет вводить имя человека, а программа - 
называть отца этого человека. Чтобы было интереснее, можно «научить» программу родственным
отношениям среди литературных персонажей, исторических лиц и современных знаменитостей. Предоставьте
пользователю возможность добавлять, заменять и удалять пары «СЫН - отец».

'''

#словарь с парами
son_dad = {'Tirion' : 'Taiwin','Aria' : 'Ned Star','Jon' : 'Raegar',
           'Jendry' : 'Robert'}

choice = None

while choice != "0":
    print(
    """
    Управление программой:
    0 - Выйти
    1 - Найти отца персонажа
    2 - Добавить пару
    3 - Изменить пару
    4 - Удалить пару
    """
    )
    choice = input("Ваш выбор: ")

    #выход
    if choice == "0":
        print("До свидания")
    #показ нужной пары
    elif choice == "1":
        son = input("Чей отец вам интересен? ")
        if son in son_dad:
            father = son_dad[son]
            print("\n", son,"имеет отца",father)
        else:
            print("\nУвы, нет данных о: ", son)
    #добавления пары
    elif choice == "2":
        son = input("Какого отпрыска вы хотите добавить? ")
        if son not in son_dad:
            father = input("\nВведите отца: ")
            son_dad[son] = father
            print("\nГерой", son, "добавлен в словарь.")
        else:
            print("\nТакой герой уже есть!")
    #изменения пары
    elif choice == "3":

        choose = None
        choose_val = None

        while not choose_val:
            choose = input('Выберите одно из имен пары, которую хотите изменить ')

            if choose in son_dad:
                choose_val = 'good'
            elif choose not in son_dad:
                for son in son_dad:
                    if son_dad[son] == choose:
                        choose_val = 'good'

        if choose_val == 'good':
            for pair in son_dad:
                if son_dad[pair] == choose:
                    father = input('Вы выбрали отца! Введите новое значение: ')
                    son_dad[pair] = father
                    print("\nГерой", pair, "был переименован в - ", father)
                    break
                elif pair == choose:
                    son = input('Вы выбрали сына! Введите новое значение: ')
                    son_dad[son] = son_dad.pop(pair)
                    print("\nГерой", pair, "был переименован в - ", son)
                    break
                
    #удаление пары
    elif choice == "4":
        son = input("Какого героя вы хотите удалить? ")
        if son in son_dad:
            del son_dad[son]
            print("\nГерой", son, "удален.")
        else:
            print("\nНичем не могу помочь. Героя ",son,"нет в словаре")

    else:
        print("В меня нет такого пункта", choice)
        
input("\n\nНажмите Enter, чтобы выйти.")

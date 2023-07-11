'''

Напишите программу «Генератор персонажей» для ролевой игры. Пользователю должно быть предоставлено
30 пунктов, которые можно распределить между четырьмя характеристиками: Сипа, Здоровье, Мудрость
и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего «Пула», 
но и возвращать их туда из характеристик, которым он решит присвоить другие значения.

'''

print("\t\t\tГенератор персонажей для ролевой игры\n")

#персонажи
chars = {}
#характеристики
stats = {'name':0,'power':0,'health':0,'wisdom':0,'dex-ty':0}

#print("\nУ вас есть ", pool,"свободных очков\n")

#print('\nХарактеристики вашего персонажа: ', '\n')

choice = None

while choice != "0":
    print(
    """

    Управление программой:
    0 - Выйти
    1 - Добавить нового персонажа
    2 - Изменить характеристики персонажа
    3 - Показать созданных персонажей
    4 - Удалить персонажа

    """
    )
    
    choice = input("Ваш выбор: ")
    
    if choice == "0":
        print("До свидания")

    #начнем с этого
    elif choice == "1":
        ID = 'id' + str(len(chars))
        pool = 30

        for sign in stats:
            if sign == 'name':
                name = input('Введите имя персонажа: ')
                stats[sign] = name
            else:
                 print(sign, end=' ')
                 while pool <= 30 and pool > 0:
                    try:
                        n = int(input())
                        if n < 0:
                            print('Только положительные числа')
                        elif (pool - n) < 0:
                            print('Слишком много!')
                        else:
                            pool -= n
                    except ValueError:
                        print('Можно вводить только числа')

                 stats[sign] = n
                
                 print('У вас закончились очки для распределения!')
                    
        chars[id] = stats

    elif choice == "2":
         change = input('Выберите id персонажа, которого вы хотите изменить: ')
         if change in chars:
            for stats in chars[change]:
                print(stats)
            new_value = input('Выберите характеристику, которую вы хотите изменить: ')
            if new_value == 'name':
                 chars[change][new_value] = input()
            else:
                chars[change][new_value] = int(input())
         else:
             print('ID отсутствует!')

    elif choice == "3":
         for id in chars:
            print(id)
            for sets in chars[id]:
                print(sets, chars[id][sets])

    elif choice == "4":
         delete = input('Введите ID персонажа, которого вы хотите удалить: ')
         if delete in chars:
            del chars[delete]
         else:
              print('ID отсутствует, либо неверный ввод!')

    else:
        print('Ошибка ввода',choice)

input('\n\nНажмите Enter, чтобы выйти')

'''
    chars = {"id_1':
            {'name':'leon',
             'power':23,
             'wisdom':21,
             'dex-ty':3
}
'''

    #нужно добавить циклы, проверки

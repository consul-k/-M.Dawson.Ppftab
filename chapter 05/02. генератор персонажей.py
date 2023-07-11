'''

Напишите программу «Генератор персонажей» для ролевой игры. Пользователю должно быть предоставлено
30 пунктов, которые можно распределить между четырьмя характеристиками: Сипа, Здоровье, Мудрость
и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего «Пула», 
но и возвращать их туда из характеристик, которым он решит присвоить другие значения.

'''

print("\t\t\tГенератор персонажей для ролевой игры\n")

#количество очков для распределения
pool = 30
#персонажи
chars = {}
#характеристики
stats = {'name':0,'power':0,'health':0,'wisdom':0,'dex-ty':0}
id = 'id'

print("\nУ вас есть ", pool,"свободных очков\n")

print('\nХарактеристики вашего персонажа: ', '\n')

for i in stats:
            stat, score = i
            print(stat, '\t\t', score)

scores = 0

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
    elif choice == "1":
        id += str(len(chars))
        pool = 30

        for sign in stats:
            if sign == 'name':
                sign = input('Введите имя персонажа: ')
            else:
                 print(sign, end=' ')
                 sign = int(input())
                 if pool > 0:
                      pool -= sign
                 elif pool <= 0:
                    print('У вас не осталось очков!')
                    
        chars[id] = stats

    #elif choice == "2":
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

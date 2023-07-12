'''

Напишите программу «Генератор персонажей» для ролевой игры. Пользователю должно быть предоставлено
30 пунктов, которые можно распределить между четырьмя характеристиками: Сипа, Здоровье, Мудрость
и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего «Пула», 
но и возвращать их туда из характеристик, которым он решит присвоить другие значения.

'''

print("\t\t\tГенератор персонажей для ролевой игры\n")

#персонажи
chars = {}

#print("\nУ вас есть ", pool,"свободных очков\n")

#print('\nХарактеристики вашего персонажа: ', '\n')


def menu():

    choice = None

    while choice != '0':
        print(
        """

        Управление программой:
        0 - Выйти
        1 - Добавить нового персонажа
        2 - Перераспределить характеристики персонажа
        3 - Показать созданных персонажей
        4 - Удалить персонажа

        """
        )
        
        choice = input("Ваш выбор: ")
        
        if choice == '0':
            print("До свидания")
        elif choice == '1':
            create()
        #elif choice == '2':
            #red_points()
        elif choice == '3':
            show()
        elif choice == '4':
            delete()
        else:
            print('Ошибка ввода!')


def create():

    identifier = 'id' + str(len(chars))
    chars[identifier] = {}

    stats = {'name':0,'power':0,'health':0,'wisdom':0,'dex-ty':0}

    name = input('Введите имя персонажа: ')
    stats['name'] = name


    def add_stats():
        
        pool = 30

        for stat in stats:
            if stat == 'name':
                continue

            print(stat, end=' ')

            if pool == 0:
                print('0 - у вас закончились очки для распределения!')
                n = 0
            else:
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
                stats[stat] = n

        if pool > 0:
            print('У вас осталось неиспользовано ', pool, 'очков')
            ask = None
            while ask != 'Y' and ask != 'N':
                ask = input('Хотите добавить их? (Y|N)').upper()
            if ask == 'Y':
                add_stats()

    add_stats()

    chars[identifier] = stats


'''
def red_points():
        identifier = None
        used_pool = []

        while identifier not in chars:
            identifier = input('Выберите id персонажа, которого вы хотите изменить: ')
            if identifier in chars:
                for stats in chars[identifier]:
                    used_pool.append(chars[identifier][stats])
                    print(stats, chars[identifier][stats])
                print('У вас осталось ', sum(used_pool),'неиспользованых очков' )

                new_value = input('Выберите характеристику, которую вы хотите изменить: ')
                while new_value not in chars[identifier]:
                     new_value = input('Данной характеристики не существует! Выберите характеристику, которую вы хотите изменить: ')

                if new_value == 'name':
                    chars[identifier][new_value] = input()
                else:
                    chars[identifier][new_value] = int(input())
            else:
                print('ID отсутствует!')
'''

def show():
    if len(chars) == 0:
        print('Нет созданных персонажей')
    for identifier in chars:
        print(identifier)
        for sets in chars[identifier]:
            print(sets, chars[identifier][sets])

        #добавить если нет созданных персонажей


def delete():
    delete = input('Введите ID персонажа, которого вы хотите удалить: ')   
    if delete in chars:
        del chars[delete]
    else:
        print('ID отсутствует, либо неверный ввод!')


            
menu()
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


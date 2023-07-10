'''

Напишите программу «Генератор персонажей» для ролевой игры. Пользователю должно быть предоставлено
30 пунктов, которые можно распределить между четырьмя характеристиками: Сипа, Здоровье, Мудрость
и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего «Пула», 
но и возвращать их туда из характеристик, которым он решит присвоить другие значения.

'''

print("\t\t\tГенератор персонажей для ролевой игры\n")

pool = 30

char = [('power',0),('health',0),('wisdom',0),('dex-ty',0)]

print("\nУ вас есть ",pool,"свободных очков\n")

print('\nХарактеристики вашего персонажа: ', '\n')

for i in char:
            stat, score = i
            print(stat, '\t\t', score)

scores = 0

choice = None

while choice != "0":
    print(
    """
    Управление программой:
    0 - Выйти
    1 - Показать персонажа
    2 - Изменить характеристики
    """
    )
    
    choice = input("Ваш выбор: ")

    print()
    
    if choice == "0":
        print("До свидания")
    elif choice == "1":
        print('Ваш персонаж\n')
        print('Характеристика\tОчки')
        for i in char:
            stat, score = i
            print(stat, '\t\t', score)
    elif choice == "2":
        pool = 30
        char = [('power',0),('health',0),('wisdom',0),('dex-ty',0)]
        for i in range(len(char)):
            new_char = char[i][0]
            print(char[i][0],'\t',end ='')
            scores = int(input())
            if scores < 0: 
                while scores < 0:
                    print('Вы ввели недопустимое количество очков',scores)
                    print(char[i][0],'\t',end ='')
                    scores = int(input())
            pool -= scores

            if pool < 0:
                pool += scores 
                print('У вас недостаточно очков для совершения этого действия, у вас осталось ', pool, 'очков')
                print(char[i][0],'\t',end ='')    
                scores = int(input())
                if scores < 0 or scores > pool:
                     while scores < 0 or scores > pool: 
                        print('Вы ввели недопустимое количество очков, ',scores,'у вас осталось', pool, 'очков')
                        print(char[i][0],'\t',end ='')
                        scores = int(input())

                pool -= scores
                    
            
            new_stat = (new_char,scores)
            char[i] = new_stat
            
            if pool == 0:
                print('\nУ вас больше нет свободных очков\n')
                break
          
    else:
        print('Ошибка ввода',choice)

    input('\n\nНажмите Enter, чтобы выйти')

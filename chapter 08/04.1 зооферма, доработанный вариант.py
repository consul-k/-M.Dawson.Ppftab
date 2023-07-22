'''

Напишите программу «Зооферма», в которой будет создано несколько объектов класса Critter, а манипулиро­
вать ими всеми можно будет с помощью списка. Теперь пользователь должен заботиться не об одной зверюш­
ке, а обо всех обитателях зоофермы. Выбирая пункт в меню, пользователь выбирает действие, которое хотел
бы выполнить со всеми зверюшками: покормить их, поиграть с ними или узнать об их самочувствии. Чтобы
программа была интереснее, при создании каждой зверюшки следует назначать ей случайно выбранные
уровни голода и уныния.

'''

#Эта версия отличается тем, что тут можно создать сколько угодно животных, кормить, играть сразу со всеми и очистить ферму

import random

class Critter(object):
    
    """Виртуальная зверушка"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        hunger = random.randint(0,7)
        self.hunger = hunger
        boredom = random.randint(0,7)
        self.boredom = boredom

def pass_time():
    for name in farm:
        farm[name]['boredom']+= 1
        farm[name]['hunger'] += 1
        


def mood(name):
    unhappiness = farm[name]['hunger'] + farm[name]['boredom']
    if unhappiness < 5:
        m = "счастливо"
    elif 5 <= unhappiness <= 10:
        m = "нормально"
    elif 11 <= unhappiness <= 15:
        m = "так себе"
    else:
        m = "ужасно"
    return m
    
def talk():
    for name in farm:
        print("Я", name, "и я чувствую себя", mood(name), "сейчас.\n")
    pass_time()

    
def feed():
    food_gain = 0
    while food_gain == 0:
        try:
            food_gain = int(input('Сколько кг. еды вы хотите дать? '))
        except:
            print('Только в цифрах!')
    print("Ммммм! Спасибо.")
    for name in farm:
        farm[name]['hunger']-= food_gain
        if farm[name]['hunger'] < 0:
            farm[name]['hunger'] = 0
    pass_time()

def play():
    fun_time = 0
    while fun_time == 0:
        try:
            fun_time = int(input('Сколько времени в минутах вы будете играть? '))
        except:
            print('Только в цифрах!')
    print("Вуиии!")
    for name in farm:
        farm[name]['boredom']-= fun_time
        if farm[name]['boredom'] < 0:
            farm[name]['boredom'] = 0
    pass_time()


def main():

    choice = None  
    while choice != "0":
        print \
        ("""
        Наша зооферма
    
        0 - Выход
        1 - Добавить животное на ферму
        2 - Узнать самочувствие зверей
        3 - Покормить питомцев
        4 - Поиграть с животинкой
        5 - Очистить ферму от всей живности бугага!
        """)
    
        choice = input("Choice: ")
        print()

        # выход
        if choice == "0":
            print("Пока-пока.")
          
        # добавить животное на ферму
        elif choice == "1":
            print('В нашей зооферме пополнение!') 
            crit_name = input("Какое имя вы дадите?: ")
            crit = Critter(crit_name)

            farm[crit_name]={'hunger':crit.hunger,'boredom':crit.boredom}

        # узнать состояние животных
        elif choice == "2":
            if len(farm) == 0:
                print('Зооферма пуста!')
            else:
                talk()
        
        # покормить животных
        elif choice == "3":
            if len(farm) == 0:
                print('Зооферма пуста!')
            else:
                feed()
         
        # поиграть с животными
        elif choice == "4":
            if len(farm) == 0:
                print('Зооферма пуста!')
            else:
                play()

        elif choice == "5":
            farm.clear()

        # другой ввод
        else:
            print("\nИзвините, но", choice, "это недоступный вариант.")

farm = {}
main()

("\n\nНажмите Enter, чтобы выйти.")

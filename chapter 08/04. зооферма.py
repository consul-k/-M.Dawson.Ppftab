'''

Напишите программу «Зооферма», в которой будет создано несколько объектов класса Critter, а манипулиро­
вать ими всеми можно будет с помощью списка. Теперь пользователь должен заботиться не об одной зверюш­
ке, а обо всех обитателях зоофермы. Выбирая пункт в меню, пользователь выбирает действие, которое хотел
бы выполнить со всеми зверюшками: покормить их, поиграть с ними или узнать об их самочувствии. Чтобы
программа была интереснее, при создании каждой зверюшки следует назначать ей случайно выбранные
уровни голода и уныния.

'''

import random

class Critter(object):
    
    """Виртуальный питомник"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        hunger = random.randint(0,7)
        self.hunger = hunger
        boredom = random.randint(0,7)
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "счастливо"
        elif 5 <= unhappiness <= 10:
            m = "нормально"
        elif 11 <= unhappiness <= 15:
            m = "так себе"
        else:
            m = "ужасно"
        return m
    
    def talk(self):
        print("Я", self.name, "и я чувствую себя", self.mood, "сейчас.\n")
        self.__pass_time()

    
    def eat(self):
        food_gain = 0
        while food_gain == 0:
            try:
                food_gain = int(input('Сколько кг. еды вы хотите дать? '))
            except:
                print('Только в цифрах!')
        print("Ммммм! Спасибо.")
        self.hunger -= food_gain
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        fun_time = 0
        while fun_time == 0:
            try:
                fun_time = int(input('Сколько времени в минутах вы будете играть? '))
            except:
                print('Только в цифрах!')
        print("Вуиии!")
        self.boredom -= fun_time
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    print('В нашей зооферме пополнение!') 
    print('\nНаш первый питомец это коза, по имени...', end=' ')
    crit_name = input("Какое имя вы дадите?: ")
    crit = Critter(crit_name)
    print('\nВторое животное, это лисичка, по имени...', end=' ')
    crit_name = input("Какое имя вы дадите?: ")
    crit1 = Critter(crit_name)
    print('\nТретье животное, это курица, по имени...', end=' ')
    crit_name = input("Какое имя вы дадите?: ")
    crit2 = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Наша зооферма
    
        0 - Выход
        1 - Узнать самочувствие зверей
        2 - Покормить питомцев
        3 - Поиграть с животинкой
        """)
    
        choice = input("Choice: ")
        print()

        # выход
        if choice == "0":
            print("Пока-пока.")

        # узнать состояние зверушки
        elif choice == "1":
            crit.talk()
            crit1.talk()
            crit2.talk()
        
        # покормить зверушку
        elif choice == "2":
            crit.eat()
            crit1.eat()
            crit2.eat()
         
        # поиграть с зверушкой
        elif choice == "3":
            crit.play()
            crit1.play()
            crit2.play()

        # другой ввод
        else:
            print("\nИзвините, но", choice, "это недоступный вариант.")

main()
("\n\nНажмите Enter, чтобы выйти.")

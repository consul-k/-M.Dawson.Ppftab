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

    farm = {}
    
    """Виртуальный питомник"""
    def __init__(self, name, species, hunger = 0, boredom = 0):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.boredom = boredom
        
        

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    '''
    def __str__(self):
        stats = 'Точные значения:\n'
        stats += '\tимя: ' + self.name + '\n'
        stats += '\tуровень голода: ' +  str(self.hunger) + '\n'
        stats += '\tуровень скуки: ' + str(self.boredom) + '\n'
        return stats
    '''

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
        print('Сколько еды вы хотите дать? ',end =' ')
        food_gain = int(input())
        print("Ммммм! Спасибо.")
        self.hunger -= food_gain
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        print('Сколько времени вы будете играть? ',end =' ')
        fun_time = int(input())
        print("Вуиии!")
        self.boredom -= fun_time
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def create(self):
        print('\tДобро пожаловать на виртуальную зооферму!')
        crit_name = input("Какое имя вы дадите?: ")
        crit = Critter(crit_name)
        crit_species = input("Какого вида это животное?: ")
        species = Critter(crit_species)
        boredom = random.randint(0,7)
        hunger = random.randint(0,7)

    #def add_farm():
        #farm
        #farm[crit_name]={'species':species, 'mood':mood, 'hungry':hungry}


def main():
     
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
        1 - Добавить новое животное на ферму
        2 - Узнать самочувствие зверей
        3 - Покормить питомцев
        4 - Поиграть с животинкой
        """)
    
        choice = input("Choice: ")
        print()

        # выход
        if choice == "0":
            print("Пока-пока.")

        # добавить животное на ферму
        elif choice == "1":
            crit.create()

        # узнать состояние животных
        elif choice == "2":
            crit.talk()
            crit1.talk()
            crit2.talk()
        
        # покормить животных
        elif choice == "3":
            crit.eat()
            crit1.eat()
            crit2.eat()
         
        # поиграть с животными
        elif choice == "4":
            crit.play()
            crit1.play()
            crit2.play()

        # другое значение 
        else:
            print("\nИзвините, но", choice, "это недоступный вариант.")

main()
("\n\nНажмите Enter, чтобы выйти")


# farm = {'Angie': {'species': goat, 'mood': 0, 'hunger': 0 } }

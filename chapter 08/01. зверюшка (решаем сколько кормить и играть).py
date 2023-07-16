'''

Доработайте программу «Моя зверюшка» так, чтобы пользователь мог сам решить, сколько еды скормить
зверюшке и сколько времени потратить на игру с ней (в зависимости от передаваемых величин зверюшка
должна неодинаково быстро насыщаться и веселеть).

'''

class Critter(object):
    #Зверюшка
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "отлично"
        elif 5 <= unhappiness <= 10:
            m = "нормально"
        elif 11 <= unhappiness <= 15:
            m = "неудовлетворительно"
        else:
            m = "в бешенстве!"
        return m
    
    def talk(self):
        print("Я", self.name, "и я чувствую себя", self.mood, "сейчас\n")
        self.__pass_time()
    
    def eat(self):
        print('Сколько еды вы дадите мне? ',end =' ')
        food_gain = int(input())
        print("Мммм! Спасибо! ")
        self.hunger -= food_gain
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        print('Сколько времени вы будете со мной играть? ',end =' ')
        fun_time = int(input())
        print("Урааа!")
        self.boredom -= fun_time
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Как вы хотите назвать зверюшку? ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Зверушка!
    
        0 - Выход
        1 - Узнать состояние зверюшки
        2 - Покормить зверюшку
        3 - Поиграть с зверюшкой
        """)
    
        choice = input("Выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания!")

        # узнать состояние зверюшки
        elif choice == "1":
            crit.talk()
        
        # Покормить зверюшку
        elif choice == "2":
            crit.eat()
         
        # Поиграть с зверюшкой
        elif choice == "3":
            crit.play()

        # другой ввод
        else:
            print("\nИзвините, но", choice, "недопустимый выбор")

main()
("\n\nНажмите Enter, чтобы выйти.")

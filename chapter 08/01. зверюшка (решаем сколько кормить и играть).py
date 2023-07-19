'''

Доработайте программу «Моя зверюшка» так, чтобы пользователь мог сам решить, сколько еды скормить
зверюшке и сколько времени потратить на игру с ней (в зависимости от передаваемых величин зверюшка
должна неодинаково быстро насыщаться и веселеть).

'''

class Critter(object):
    #Зверушка
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
        food_gain = 0
        while food_gain == 0:
            try:
                food_gain = int(input('Сколько кг. еды вы хотите дать? '))
            except:
                print('Только в цифрах!')
        print("Мммм! Спасибо!")
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
        print("Урааа!")
        self.boredom -= fun_time
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Как вы хотите назвать зверушку? ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Зверушка!
    
        0 - Выход
        1 - Узнать состояние зверушки
        2 - Покормить зверушку
        3 - Поиграть с зверушкой
        """)
    
        choice = input("Выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания!")

        # узнать состояние зверушки
        elif choice == "1":
            crit.talk()
        
        # покормить зверушку
        elif choice == "2":
            crit.eat()
         
        # поиграть с зверушкой
        elif choice == "3":
            crit.play()

        # другой ввод
        else:
            print("\nИзвините, но", choice, "недопустимый выбор")

main()
("\n\nНажмите Enter, чтобы выйти.")

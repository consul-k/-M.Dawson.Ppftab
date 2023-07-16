'''

Создайте программу, имитирующую телевизор как объект. У пользователя должна быть возможность вводить
номер канала, а также увеличивать и уменьшать громкость. Программа допжна следить за тем, чтобы номер
канала и уровень громкости оставались в допустимых пределах.

'''

# Виртуальный телевизор

class TV(object):
    """Виртуальный ТВ"""

    def __init__(self, chanel = 1, volume = 4):
        self.chanel = chanel
        self.volume = volume
    
    def vol(self):
        vol = None
        while not vol:
            try:
                vol = int(input('Уровень громкости: '))
            except ValueError:
                print('Недопустимый ввод! Сделайте выбор 1-10')
        
        if vol < 0:
            vol = 0
        elif vol > 10:
            print('Достигнута максимальная громкость - 10')
            vol = 10  
        self.volume = vol


    def chan(self):

        chanel = None

        while not chanel:
            try:
                chanel = int(input('Доступно 5 каналов. Выберете номер канала: '))
            except ValueError:
                print('Недопустимый ввод! Сделайте выбор 1-5')
        if chanel <= 0:
            chanel = 1
        elif chanel > 5:
            print('Больше каналов нет! Выбран крайний!')
            chanel = 5
            
        if chanel == 1:
            chanel = 'Рогатые и пернатые'
        elif chanel == 2:
            chanel = 'Малолетние алкоголички'
        elif chanel == 3:
            chanel = 'Новости нашего городка'
        elif chanel == 4:
            chanel = 'Для маленьких обосранцев'
        elif chanel == 5:
            chanel = 'Рен ТВ, канал для психов'
        else:
            print('\nДанный канал отсутствует. Введите правильный номер: ')
        self.chanel = chanel
        print('\nКанал: ',chanel)
        
    
    def __str__(self):
        stats = 'Инфо\n'
        stats += 'Канал: ' + str(self.chanel) + '\n'
        stats += 'Громкость: ' + str(self.volume) + '\n'
        return stats
        
    
def main():
    tv = TV()
    choice = None
    while choice != 0:
        print \
        ("""
        Виртуальный телевизор

        0 - Выход
        1 - Выбор канала
        2 - Выбор громкости
        3 - Текущий просмотр
        """)

        print()

        try:
            choice = int(input("Выбор: "))
        except ValueError:
            print("Недопустимый ввод! Сделайте выбор в допустимых значениях")

        print()

        # выход
        if choice == 0:
            print('Отключение')
            
        # канал
        elif choice == 1:
            tv.chan()
            
        # громкость
        elif choice == 2:
            tv.vol()

        # текущий просмотр
        elif choice == 3:
            print(tv)

        # неизвестный выбор

        else:
            print('\nИзвините, но', choice, 'недоступный вариант')

main()

('\n\nНажмите Enter, чтобы выйти')

'''

Создайте несnожную объектно-ориентированную приключенческую игру, в которой игрок сможет менять свое
местонахождение, перемещаясь каждый раз в одно из мест, ближайших к данному.

'''

class Player(object):
    ''' Игрок '''
    def __init__(self, name, location = 'Земля'):
        self.name = name
        self.location = location

    def __str__(self):
        rep = 'имя: ' + self.name + '\n' + 'локация: ' + str(self.location) + '\n'
        return rep

    def move(self, title):
        self.location = title
        
    

class Solar_system(object):

    PLANETS = {'Меркурий':'\nСлишком жарко днем, который длится пол года, очень холодно ночью, которая длится пол года, нет воздуха и воды.\n',
               'Венера':'\nПарниковый эффект не так уж страшен говорили они! И посмотрите на Венеру!\n',
               'Земля':'\nРодной райский мир.\n',
               'Марс':'\nТам так скучно, что даже выращивание картошки заменяет поход в ночной клуб.\n',
               'Европа':'\nВозможно тут есть жизнь, а вы как тюлень будете искать ждать у проруби...\n',
               'Титан':'\nХотите поплавать в метановом море? Говорят в этом году это модный курорт!\n',
               'Уран':'\nПрыжок в этот сгусток газов будет самым затяжным в вашей жизни\n',
               'Нептун':'\nКак и в случае с Ураном, лучше не искать тут почву под ногами...\n',
               'Плутон':'\nВы только посмотрите, кто возомнил себя планетой\n'}

    def __init__(self, planets):
        self.planets = PLANETS
        
    def planet(self, title):
        title = None
        while title not in PLANETS:
            title = str(input('Ну так куда же летим? '))
        return 

def ask_yes_no(question):
    response = None
    while response not in ('да','нет'):
        response = input(question).lower()
    return response


print('Добро пожаловать в простенькую игру о перемещении по Солнечной системе!\n')
name = input('Введите ваше имя: ')
player = Player(name)
print('\nИтак, ваш текущий статус: ')
print(player)
title = None
again = None
while again != 'нет':
    again = ask_yes_no('\nСлетам куда-нибудь? (да/нет) ').lower()
    if again == 'да':
        print('\nВот куда мы можем полететь: \n')
        for planet in Solar_system.PLANETS:
            print('\t'+planet)
        while title not in Solar_system.PLANETS:
            title = str(input('\nКуда летим? '))
        print(Solar_system.PLANETS.get(title)+'\n')
        player.move(title)
        

input('\nНажмите Enter, чтобы выйти.')

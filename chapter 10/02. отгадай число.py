'''
  
Перепишите игру «Отгадай число» из главы 3: создайте для нее графический интерфейс.
  
'''

import random
from tkinter import *

class Application(Frame):
    ''' Игра "Отгадай число" '''
    def __init__(self, master):
        ''' Инициализируем рамку '''
        super(Application, self).__init__(master)
        self.grid()
        self.tries = 7
        self.riddle = None
        self.number()
        self.create_widgets()

    def create_widgets(self):
        ''' Создаем кнопку, текстовое поле, текстовую область '''
        Label(self,
              text = "Добро пожаловать в 'Отгадай число'!"
              ).grid(row = 0,column = 0, sticky = W)
        Label(self,
              text = "Я думаю о числе между 1 и 100..."
              ).grid(row = 1,column = 0, sticky = W)
        Label(self,
              text = "Постарайтесь отгадать его за 7 попыток."
              ).grid(row = 2,column = 0, sticky = W)

        #Метка число около ввода
        self.pw_lbl = Label(self, text = 'Число: ')
        self.pw_lbl.grid(row = 3, column = 0, sticky = W)

        #текстовое поле для ввода числа
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 3, column = 1, sticky = W)

        #Кнопка
        self.submit_bttn = Button(self, text = 'Проверить', command = self.reveal)
        self.submit_bttn.grid(row = 4, column = 0, sticky = W)

        #текстовая область для вывода
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 5, column = 0, columnspan = 2, sticky = W)


    def update_tries(self):
        self.tries -= 1

    def number(self):
        self.riddle = random.randint(1, 100)

    def reveal(self):
        guess = self.pw_ent.get()
        self.update_tries()
        guess = int(guess)

        if self.tries != 0:
            if guess == self.riddle:
                message = "Вы угадали!  Это число было " + str(self.riddle) + " и это стоило вам" + str(self.tries) + " попыток"
            elif guess > self.riddle:
                message = "Меньше... У вас осталось " + str(self.tries) + " попыток"
            elif guess < self.riddle:
                message = "Больше... У вас осталось " + str(self.tries) + " попыток"
        else:
            message = 'У вас не осталось попыток, увы, вы проиграли'

        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)
            


#main
root = Tk()
root.title('Отгадай число')
app = Application(root)
root.mainloop()

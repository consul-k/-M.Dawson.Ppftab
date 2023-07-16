'''

Напишите программу «Счет, пожалуйста!». Она должна показать пользователю несложное ресторанное меню
с блюдами и ценами, принять его заказ и вывести на экран сумму счета.

'''

from tkinter import *

class Application(Frame):
    ''' Ресторанное меню '''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.bill = 0
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        ''' Создает элементы выбора и кнопку заказа '''
        Label(self,
              text = 'Ознакомьтесь с нашим меню и сделайте заказ'
              ).grid(row = 0, column = 0, sticky = W)
        Label(self,
              text = 'Выберите все, что вам по вкусу:'
              ).grid(row = 1, column = 0, sticky = W)

        #флажок 'Вода из лужи'
        self.water = BooleanVar()
        Checkbutton(self,
                    text = 'Вода из лужи',
                    variable = self.water,
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)
        
        #флажок 'Сладкий перчик'
        self.perch = BooleanVar()
        Checkbutton(self,
                    text = 'Сладкий перчик',
                    variable = self.perch,
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)
        
        #флажок 'Булочка с тараканами'
        self.buloch = BooleanVar()
        Checkbutton(self,
                    text = 'Булочка с тараканами',
                    variable = self.buloch,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)
        

        #флажок 'Курочка на палочке'
        self.chick = BooleanVar()
        Checkbutton(self,
                    text = 'Курочка на палочке',
                    variable = self.chick,
                    command = self.update_text
                    ).grid(row = 5, column = 0, sticky = W)
        
        #флажок 'Забродившее яблочко'
        self.apple = BooleanVar()
        Checkbutton(self,
                    text = 'Забродившее яблочко',
                    variable = self.apple,
                    command = self.update_text
                    ).grid(row = 6, column = 0, sticky = W)


        #Кнопка
        self.submit_bttn= Button(self, text = 'Счет, пожалуйста!', command = self.check)
        self.submit_bttn.grid(row = 7, column = 1, sticky = W)

        # текстовая область с результатами
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 8, column = 0, columnspan = 4)


    def update_text(self):

        self.bill = 0

        if self.water.get():
            self.bill += 30

        if self.perch.get():
            self.bill += 50

        if self.buloch.get():
            self.bill += 45

        if self.chick.get():
            self.bill += 80

        if self.apple.get():
            self.bill += 50

    
    def check(self):
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.bill)
        self.bill = 0

                
root = Tk()
root.title('Счет, пожалуйста!')
app = Application(root)
root.mainloop()

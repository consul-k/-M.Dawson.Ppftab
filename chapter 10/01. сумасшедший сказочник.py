'''

Напишите собственную версию «Сумасшедшего сказочника>>, в которой система элементов управления внутри
окна будет другой.

'''

from tkinter import *

class Application(Frame):
    ''' Это великий генератор шуток '''
    def __init__(self, master):
        ''' Инициализируем рамку '''
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        ''' Создаем элементы для выбора '''
        # метка-инструкция
        Label(self,
              text = 'Собери себе шутку'
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        # Текстовое поля для имени
        Label(self,
              text = 'Кто:'
              ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)

        # Метка для описания "Приходит"
        Label(self,
              text = 'Приходит:'
              ).grid(row = 2, column = 0, sticky = W)

        # создаем варианты
        self.come = StringVar()
        self.come.set(None)

        # создаем кнопки для выбора
        come_variants = ['в офис',
                         'в небытие',
                         'в лабораторию',
                         'на родительское собрание',
                         'к кошке']
        column = 1
        for come in come_variants:
            Radiobutton(self,
                        text = come,
                        variable = self.come,
                        value = come
                        ).grid(row = 2, column = column, sticky = W)
            column += 1


        # метка для описания "И говорит"
        Label(self,
              text = 'И говорит:'
              ).grid(row = 3, column = 0, sticky = W)
        
        # флажок пика-пика
        self.pika = BooleanVar()
        Checkbutton(self,
                    text = 'пика-пика',
                    variable = self.pika
                    ).grid(row = 3, column = 1, sticky = W)
        # флажок я мама вовочки
        self.mam = BooleanVar()
        Checkbutton(self,
                    text = 'я мама вовочки',
                    variable = self.mam
                    ).grid(row = 3, column = 2, sticky = W)
        # флажок давай заведем котят
        self.cats = BooleanVar()
        Checkbutton(self,
                    text = 'давай заведем котят',
                    variable = self.cats
                    ).grid(row = 3, column = 4, sticky = W)
        # флажок какой серьезный засор
        self.mess = BooleanVar()
        Checkbutton(self,
                    text = 'какой серьезный засор',
                    variable = self.mess
                    ).grid(row = 3, column = 5, sticky = W)
        # флажок аллах акбар
        self.rar = BooleanVar()
        Checkbutton(self,
                    text = 'ррраар ррраар',
                    variable = self.rar
                    ).grid(row = 3, column = 6, sticky = W)


        # создаем кнопку для получения шутки
        Button(self,
               text = 'Собрать шутку',
               command = self.tell_joke
               ).grid(row = 4, column = 0, sticky = W)

        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 5, column = 0, columnspan = 6)


    def tell_joke(self):
        ''' Заполним текстовую область историей '''
        # получаем значения из GUI
        person = self.person_ent.get()
        come = self.come.get()
        tell = ''
        if self.pika.get():
            tell += ' пика-пика'
        if self.mam.get():
            tell += ' я мама вовочки'
        if self.cats.get():
            tell += ' давай заведем котят'
        if self.mess.get():
            tell += ' какой серьезный засор'
        if self.rar.get():
            tell += ' ррраар ррраар'

        # создаем шутку
        joke = ''
        joke += person
        joke += ' приходит '
        joke += come
        joke += ' и говорит: '
        joke += tell
        joke += '. Так появилась вселенная'

        # отображаем шутку
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, joke)

        
              
#main
root = Tk()
root.title('Конструктор шуток')
app = Application(root)
root.mainloop

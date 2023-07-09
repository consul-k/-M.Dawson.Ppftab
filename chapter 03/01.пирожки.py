import random
print ("\t\t\tСимулятор пирожка с 'Cюрпризом'")

mood = random.randint(0,4)
list_ing = ['с тараканами', 'c вишней', 'с мухами', 'c ветчиной и сыром', 'c слезами вашего врага!']
print ("\nИтак, ваш пирожок... " + list_ing[mood], '\n')

input("\n\nНажмите Enter чтобы выйти.")

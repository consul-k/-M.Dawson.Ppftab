import random
print ("\t\t\tСимулятор пирожка с 'Cюрпризом'")
print ("\nИтак, ваш пирожок...", end=" ")
mood = random.randint(1,5)
if mood == 1:
    print ("с тараканами")
elif mood == 2:
    print ("c вишней")
elif mood == 3:
    print ("с мухами")
elif mood == 4:
    print ("c ветчиной и сыром")
elif mood == 5:
    print ("c слезами вашего врага!")
input("\n\nНажмите Enter чтобы выйти.")

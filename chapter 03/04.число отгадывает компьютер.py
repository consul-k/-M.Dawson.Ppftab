import random  

print("\tДобро пожаловать в 'Борьбу интуиций'!")
print("\nЯ загадываю компьютеру число между 1 и 100 и запрещаю подглядывать!")
print("Компьютер пробует отгадать его за 7 попыток.\n")


the_number = int(input("Мое число: "))
guess = random.randint(1, 100)
tries = 1


while guess != the_number and tries < 7:
    print("Компьютер: ", guess)
    if guess > the_number:
        guess = random.randint(1, the_number)
        input("Человек: Меньше... Даю тебе еще один шанс ")
    else:
        guess = random.randint(the_number, 100)
        input("Человек: Больше... Даю тебе еще один шанс")

    tries += 1
    if tries == 7:
        break
    
if guess == the_number:
    print("\nСкайнет уже в пути!  Это число было", the_number)
    print("И это стоило всего", tries, "попыток!\n")
else:
    print("\nЖелезный дубина проиграл кожанному мешку! И это стоило тебе", tries, "попыток!")
  
input("\n\nНажмите Enter, чтобы выйти.")

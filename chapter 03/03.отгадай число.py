import random  

print("\tДобро пожаловать в 'Отгадай число'!")
print("\nЯ думаю о числе между 1 и 100...")
print("Постарайтесь отгадать его за 7 попыток.\n")


the_number = random.randint(1, 100)
guess = int(input("Ваша догадка: "))
tries = 1


while guess != the_number and tries < 7:
    if guess > the_number:
        print("Меньше...")
    else:
        print("Больше...")
            
    guess = int(input("Ваша догадка: "))
    tries += 1
    if tries == 7:
        break
    
if guess == the_number:
    print("Вы угадали!  Это число было", the_number)
    print("И это стоило всего", tries, "попыток!\n")
else:
    print("Ты проиграл компьютеру, кожанный мешок! И это стоило тебе", tries, "попыток!")
  
input("\n\nНажмите Enter, чтобы выйти.")

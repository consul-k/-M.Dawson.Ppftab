'''
  
Доработайте функцию ask_number() так, чтобы ее можно было вызывать еще с одним параметром -
кратностью (величиной шага). Сделайте шаг по умолчанию равным 1.

Доработайте новую версию игры «Опадай число» (которую вы создали, решая предыдущую задачу) так, чтобы
основная часть программы стала функцией main(). Для того чтобы игра началась, не забудьте вызвать эту
функцию глобально.
  
'''
  

import random  

#инструкция

def display_instruct():
    print("\tДобро пожаловать в 'Отгадай число'!",
          "\nЯ думаю о числе между 1 и 100...",
          "\nПостарайтесь отгадать его за 7 попыток.\n")

#создаем загаданное число
def the_number():
    global number
    number = random.randint(1, 101)
    return(number)

tries = 1
guess = 0

#спрашиваем число
def ask_number():
    global guess
    global tries
    guess = int(input("Ваша догадка: "))
    while guess != number or tries < 7:
        if guess == number:
            break
        elif guess > number:
            print("Меньше...")
        else:
            print("Больше...")
        guess = int(input("Ваша догадка: "))
        tries += 1
        if tries == 7:
            break

    return guess

def congrat():
    
    if guess == number:
        print("Вы угадали!  Это число было ", number,
        ", и это стоило всего", tries, "попыток!\n")
    else:
        print("Ты проиграл компьютеру, кожанный мешок! И это стоило тебе", tries, "попыток!")


def main():
    display_instruct()
    number = the_number()
    ask_number()
    congrat()
    

main()
input("\n\nНажмите Enter, чтобы выйти.")

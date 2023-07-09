import random

WORDS = ("питон", "город", "муравей", "паук", "ответ", "овсянка", "рынок")

word = random.choice(WORDS)
correct = word


jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]


print(
"""
           Доработанная версия игры "Анаграммы"!
        
       Расшифруйте загаданное слово.
(Press the enter key at the prompt to quit.)
"""
)
print("Анаграмма:", jumble)

score = 10                              # счетчик очков 
count_a = 0                             # счетчик попыток
guess = input("\nВаша догадка: ")

if guess != "":
    count_a+=1
    
while guess != correct and guess != "":
    if count_a == 0 or count_a == 1:
        print("Увы, не угадали.")
    guess = input("Ваша догадка: ")
    if guess != correct and guess != "":
        print("Увы, не угадали.")
    count_a+=1
    if count_a == 7:
        ans = input("Вы хотите воспользоваться подсказкой? ") #ответ на вопрос
        if ans == "Да" or ans == "да":
            score -=5
            print("Первая буква - ", correct[0], "последняя - ", correct[-1])
            count_a = 2
        elif ans == "Нет" or ans == "" or ans == "нет":
            print("Удачи! Наберитесь терпения")
            count_a = 2
    
if guess == correct:
    print("Это оно! Вы угадали!\n")
    print("И вы заработали ", score, "очков")


    

print("Спасибо за игру.")

input("\n\nНажмите Enter, чтобы выйти.")

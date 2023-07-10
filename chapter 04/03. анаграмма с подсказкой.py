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

У вас есть 10 попыток!
Если вы желаете воспользоваться подсказкой напишите help

"""
)
print("Анаграмма:", jumble)

guess = ''
score = 100                              # счетчик очков 
count_a = 0                             # счетчик попыток

while guess != correct and count_a < 10:
    guess = input("\nВаша догадка: ")
    count_a+=1
    if guess == correct:
        break
    elif guess != correct and guess.lower() != 'help':
        print("\nУвы, не угадали.")
        score -= 5
    elif guess.lower() == 'help':
        score -= 30
        print("Первая буква - ", correct[0], "последняя - ", correct[-1])

if count_a == 10:
    print('\nК сожалению вы проиграли!')
else:
    print("\nЭто оно! Вы угадали!\n")
    print("И вы заработали ", score, "очков ",'и вам потребовалось ', count_a, 'попытки')

print("\nСпасибо за игру.")

input("\n\nНажмите Enter, чтобы выйти.")

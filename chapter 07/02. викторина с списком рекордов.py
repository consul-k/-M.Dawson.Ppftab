'''

Доработайте игру «Викторина» таким образом, чтобы она хранила в файле список рекордов. В список доnжны
попадать имя и результат игрока-рекордсмена. Используйте для хранения таблицы рекордов консервирован­ный объект.

'''

import sys, pickle

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    #вот тут должна быть строка с очками
    
    if correct:
        correct = correct[0]
        score = next_line(the_file)
    else:
        score = 0
        
    explanation = next_line(the_file) 

    return category, question, answers, correct, score, explanation

def record_list():
    names = []
    scores = []

    name = input('Введите ваше имя: ')
    names += [name]
    scores += [score_pool]
    records = dict(zip(names,scores))

    f = open('records.dat', 'ab')
    pickle.dump(records,f)
    f.close()

    ask = None
    while ask != 'Y' and ask != 'N':
        ask = input('Хотите увидеть другие рекорды? (Y|N) ').upper()
    if ask == 'Y':
        f = open('records.dat', 'rb')
        while True:
            try:
                s = pickle.load(f)
            except EOFError:
                break
            else:
                print(s)
        

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    global score_pool
    score_pool = 0
    score = 0

    # get first block
    category, question, answers, correct, score, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score_pool += int(score)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score_pool, "\n\n")

        # get next block
        category, question, answers, correct, score, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score_pool)
    
 
main()
record_list()

input("\n\nPress the enter key to exit.")

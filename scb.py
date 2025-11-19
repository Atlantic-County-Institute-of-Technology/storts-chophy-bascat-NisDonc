# reading_words.py
# author: Nisdalie Doncell
# created : 11.3.25, 9:58 am
# last updated : 11.5.25, 10:00 am
# description : project demostrating file io with the text file "words_alph
# a.txt"


import random
import os

# word_len = 5
#
#
# word_list = []


diff_length = 0
def populateworld_list():
    word_list = []
    with open("assets/words_alpha.txt") as file:
        for word in file.readlines():
            if len(word.strip()) == diff_length:
                word_list.append(word.strip())
        value = random.choice(word_list)
        return str(value)


def game():
    try_number = 0
    win = False
    target = populateworld_list()
    while try_number < diff_length and not win:

        print(f"Target is:{target}")  # string/list
        print(f"Tries Remaining: {diff_length - try_number}")
        guess = ""
        while len(guess) != diff_length:
            guess = input("please enter your word guess!.").lower()
        response = ["bascat" for i in range(len(target))]

        if guess == target:
            win = True
            print("Yay! You solved the puzzle")

        else:
            for g_digit in range(len(guess)):
                for t_digit in range(len(target)):
                    if guess[g_digit] == target[t_digit]:
                        if g_digit == t_digit:
                            response[g_digit] = "Chophy"
                        else:
                            response[g_digit] = "Storts"
                            print(response)
        try_number += 1

    if not win:
        print("L ratio get good loser :P")
    else:
        print("Congrats!")



def main():
    print("WORDLE first input your difficulty")
    while True:
        global diff_length
        diff_length = int(input("how long would u want your word?"))
        populateworld_list()
        print("1 - exit 2 - play")
        LIST_SELECTION = int(input("type here:"))
        if LIST_SELECTION == 1:
            exit()
        elif LIST_SELECTION == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            game()

if __name__ == '__main__':
    main()

# read in the file words_alpha.txt
# add every WORD_LENGTH word to a list
# randomly pick out a word from that list to be our target
# if len(word) == WORD_LENGTH

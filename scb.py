# reading_words.py
# author: Nisdalie Doncell
# created : 11.3.25, 9:58 am
# last updated : 11.5.25, 10:00 am
# description : project demostrating file io with the text file "words_alph
# a.txt"


import random
# word_len = 5
#
#
# word_list = []

word_list = []

word_length = int(input("how long would u want your word?"))
def populateworld_list():
    with open("assets/words_alpha.txt") as file:
        for word in file.readlines():
            if len(word.strip()) == word_length:
                word_list.append(word.strip())
                value = random.choice(word_list)
                return str(value)

def main():
    target = populateworld_list()
    print(f"Target is:{target}") #string/list

    guess = input("please enter your word guess!.")
    response = ["bascat" for i in range (len(target))]

    if guess == target:
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

if __name__ == '__main__':
    main()

#
#
#


# read in the file words_alpha.txt
# add every WORD_LENGTH word to a list
# randomly pick out a word from that list to be our target



# if len(word) == WORD_LENGTH


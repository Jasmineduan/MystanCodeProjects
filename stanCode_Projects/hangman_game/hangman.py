"""
File: hangman.py
Name: Jasmine Duan
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Users see a dashed word, trying to correctly figure the un-dashed word out by inputting one character each round.
    """
    s = random_word()
    word_num = count_num(s)
    print('The word looks like ' + str(word_num))
    print('You have ' + str(N_TURNS) + ' wrong guesses left.')
    dash_word = check_ch(s, word_num)
    result(dash_word, s)


def count_num(word):
    """
    : param: str, user input the word
    : return: str, change the word to dash
    """
    ans = ''
    for ch in word:
        ans += '-'
    return ans


def check_ch(word, dash_word):
    """
    : param: str, user input the word
    : param: str, dashed word
    : return: str, final word
    """
    count = N_TURNS
    while count > 0 and word != dash_word:
        input_ch = input('Your guess: ')
        if input_ch.isalpha() and len(input_ch) == 1:
            input_ch = input_ch.upper()
            if input_ch in word:
                dash_word = check_word(word, dash_word, input_ch)
                print('You are correct!')
                count -= 0
            else:
                count -= 1
                print('There is no ' + input_ch + "'s in the word")
            print('You have ' + str(count) + ' wrong guess left.')
            print('The word looks like ' + dash_word)
        else:
            print('Illegal format.')
    return dash_word


def check_word(word, dash_word, input_ch):
    """
    : param: str, user input the word
    : param: str, dashed word
    : param: str, single word
    : return: str, final word
    """
    ans = ''
    for i in range(len(word)):
        if word[i] == input_ch:
            ans += input_ch
        else:
            ans += dash_word[i]
    return ans


def result(dash_word, s):
    """
    : param: str, dashed word
    : param: str, random word
    : return: str, final answer
    """
    if dash_word.isalpha():
        print('You win!!')
    else:
        print('You are completely hung : (')
    print('The word was: ' + s)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

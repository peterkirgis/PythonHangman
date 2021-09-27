#!/Users/peterkirgis/Documents/6-0001-fall-2016/6-0001-fall-2016/contents/assignments/ps2/HangmanVersion.py python3


# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:31:02 2021

@author: peterkirgis
"""

print("Welcome to my hangman game!")

import random

WORDLIST_FILENAME = "words.txt"
inFile = open(WORDLIST_FILENAME, 'r')
line = inFile.readline()
wordlist = line.split()

secret_word = random.choice(wordlist)
lengthword = len(secret_word)
print("Your Word has " + str(lengthword) + " letters")
current_guess = ""
letters_guessed = []
no_of_guesses = 6

while no_of_guesses > 0:
    guess = input("What is your next guess?")
    if len(guess) >= 2:
        print("Guess must be only one character")
        guess = input("What is your next guess?")
    elif guess in letters_guessed:
        print("You've alredady guessed that letter!")
        guess = input("What is your next guess")
    else:
        guess = guess
    letters_guessed.append(guess)
    for let in guess:
        if let not in secret_word:
            print(let + " was not in the word")
            no_of_guesses = no_of_guesses - 1
        else:
            print(let + " was in the word")
    new_guess = ""        
    for ele in secret_word:
        if ele in letters_guessed:
            new_guess += ele
        else:
            new_guess += "_ "
    current_guess = new_guess
    new_guess = ""
    print("You've gotten these letters " + current_guess)
    print("You've guessed " + str(letters_guessed))
    if current_guess == secret_word:
        print("You got all the letters! The word is " + secret_word)
        break
    elif no_of_guesses == 0:
        print("You are out of guesses! The word was" + secret_word + ". Game over :(")
        break
    else:
        print("You have " + str(no_of_guesses) + " remaining!")
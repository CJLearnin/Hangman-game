import os 
import random
import sys


words = [
'apples',
'pears',
'grapes',
'oranages'
]

def clear():
    if os.name --'nt':
        os.system('cls')
    else:
        os.system('clear')
    


def draw(bad_guess, good_guess, secret_word):
    clear()
    print('strikes:{}/7'.format(len(bad_guess)))
    print('')
    
    for letter in bad_guess:
        print(letter,end=' ')
    print('\n\n')   
              
    for letter in secret_word:
        if letter in good_guess:
            print(letter, end=' ')
        else:
            print('_',end='')
              
    print(' ')
                    
    
def get_guess(bad_guess, good_guess):
    while True:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1:
            print("you can only guess a single letter!")
        elif guess in bad_guess or guess in good_guess:
            print("you have already guessed that letter:")  
        elif not guess.isalpha():
            print("you can only guess letters!")    
        else:
            return guess
def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guess = []
    good_guess = []
    
    while True:
        draw(bad_guess, good_guess, secret_word)
        guess = get_guess(bad_guess,good_guess)
        if guess in secret_word:
            good_guess.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guess:
                    found = False
            if found:
                print("you win!")
                print("The secret word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guess, good_guess, secret_word)
                print("You lost! =(")
                print("The secret word was {}".format(secret_word))
                done = True
                
                
        if done:
            play_again = input("play again? Y/n ".lower()
            if play_again != 'n'
                return play(done=False)               
            else:
                sys.exit()              
while True:
    start = input("Press enter/return to start, or enter Q to quit")
    if start.lower() == 'q':
        print("goodbye!")
        break
        
    secret_word = random.choice(words)
    bad_guess = []
    good_guess = []
    
    while len(bad_guess) < 7 and len(good_guess) != len(list(secret_word)):
        if guess in secret_word:
            good_guess.append(guess)
            if len(good_guess) == len(list(secret_word)):
                print("You win! the word was {}".format(secret_word))
                break
        else:
            bad_guess.append(guess) 
    else:
        print("you lose! the word was {}.".format(secret_word))
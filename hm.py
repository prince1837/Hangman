import string
from words import choose_word
from images import IMAGES
def is_word_guessed(secret_word, letters_guessed):
    if secret_word == get_guessed_word(secret_word, letters_guessed):
        return True

    return False
def ifvalid(user_input):
    if len(user_input)!=1:
        return False
    if not user_input.isalpha():
        return False
    return True
def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
def get_available_letters(letters_guessed):
    import string
    all_letters = string.ascii_lowercase
    letters_left = ""

    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left += letter
    
    return letters_left
def get_hint(secret_word, letters_guessed):
    import random
    letters_not_guessed = []
    
    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)

        index += 1

    return random.choice(letters_not_guessed)
def hangman(secret_word):
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print ""
    letters_guessed = []
    total_lives=remaining_lives=8
    images_selection=[0,1,2,3,4,5,6,7]
    level = raw_input("enter the level in which level you wants to play\n""a for easy\n""b for medium\n""c for hard\n")
    if level=="b":
        total_lives=remaining_lives=6
        images_selection=[1,2,3,4,6,7]
    elif level=="c":
        total_lives=remaining_lives=4
        images_selection=[1,3,5,7]
    else:
        if level!= "a":
            print "your choice is invalid \n ""game is starting in easy level"
    while (remaining_lives>0):
        available_letters = get_available_letters(letters_guessed)
        print "Available letters: " + available_letters
        guess = raw_input("Please guess a letter: ")
        if guess == "hint":
                letter = get_hint(secret_word, letters_guessed)
                letters_guessed.append(letter)
                print ( get_guessed_word(secret_word, letters_guessed))
        else:
            letter = guess.lower()
            if (not ifvalid(letter)):
                print "aapka input invalid hai"
                continue
            if letter in secret_word:
                letters_guessed.append(letter)
                print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
                print ""
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print " * * Congratulations, you won! * * "
                    print ""
                    break
            else:
                print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
                letters_guessed.append(letter)
                print IMAGES[images_selection[total_lives-remaining_lives]]
                remaining_lives-=1
                print remaining_lives
                print ""
    else:
        print "sorry you lose the game, the word was", + secret_word
secret_word = choose_word()
hangman(secret_word)


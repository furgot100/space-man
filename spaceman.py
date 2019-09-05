import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass
    for letters in secret_word:
        if letters in letters_guessed:
            continue
        else:
            return False
        
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    dashes = "_" * len(secret_word)
    
    result = ""
    
    for i in range(len(secret_word)):
        if secret_word[i] == letters_guessed:
            result = result + letters_guessed

        else:
            result = result + dashes
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    # pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        print("Letter is in word")

    else:
        print("Letter is not in the word")
    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_left = list('abcdefghijklmnopqrstuvwxyz')
    print("".join(letters_left))
    #TODO: show the player information about the game according to the project spec
    print("Letters left: " + letters_left)
    
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    letters_guessed = list()
    while len(letters_left) < 27:
        guess = input("Enter a letter: ")
        if len(guess) != 1:
            guess = input("Enter a letter again: ")
            letters_guessed.append(guess)
        else:
            letters_guessed.append(guess)
   
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    print(is_guess_in_word(guess,secret_word))
    
    #TODO: show the guessed word so far
    print(get_guessed_word(secret_word,guess))
    
    #TODO: check if the game has been won or lost
    if is_word_guessed == True:
        print("You lose! the word is " + str(secret_word))
    else:
        print("You win! The word was " + str(secret_word))
    
    
    

    

   





#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
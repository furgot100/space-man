import random
import string

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
    #dashes = "_" * len(secret_word)
    
    
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    pass
    result = ""
    for letters in secret_word:
        if letters in letters_guessed:
            result += letters
        else:
            result += "_"
    return result


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
       return True
    else:
        return False
    
    
    pass



def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed =list()
    tries = 7
    letters_left = list(string.ascii_lowercase)
    
    while tries > 0:
        print('---------------------')
        #print(secret_word)

        guess = str(input('Enter a letter: '))

        while len(guess) != 1:
            guess = str.lower(input('Enter one letter'))

        while str.isalpha(guess) == False:
            guess = str.lower(input('C\'mon man. A letter:'))
            #letters_guessed.append(guess)

        while guess in letters_guessed:
            guess = str.lower(input('Letter already used. Try again.'))


        letters_guessed.append(guess)
        
        print(get_guessed_word(secret_word, letters_guessed))

        if is_guess_in_word(guess,secret_word) == True:
            print('Correct!')
        else:
            print("Incorrect, try again")
            tries -= 1

        print('Letters guessed so far: ', *letters_guessed)

        letters_left.remove(guess)
        print("Tries left: ", tries)
        print("Letters left: ", *letters_left)

        if is_word_guessed(secret_word, letters_guessed) == True:
            return print("You win!")
        
        if tries < 1:
            print("You lose!, the word was", secret_word)
        

        

    
        
    #while is_word_guessed(secret_word, letters_guessed) == True:
        #print("You win!")
        #break
        
    #if is_word_guessed(secret_word, letters_guessed) == False:
        #print("You lose!, the word was", secret_word)
   
    
    
    #TODO: show the player information about the game according to the project spec
    
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    
    #TODO: show the guessed word so far
    
    #TODO: check if the game has been won or lost
    
    #GeeksforGeeks helping with lower case alphabet
#These function calls that will start the game. uncomment to begin
# secret_word = load_word()
# print("The word contains: " + str(len(secret_word)) + "letters")
# spaceman(secret_word)    



def test_is_guess_in_word():
    assert is_guess_in_word('a','apple') == True
    assert is_guess_in_word('a', 'dog') == False
    assert is_guess_in_word(',','dog') == False

def test_is_word_guessed():
    assert is_word_guessed('apple', ['a','p','l','e']) == True
    assert is_word_guessed('dog', ['d','o']) == False
    assert is_word_guessed('sleep',['e','p','s']) == False

def test_get_guessed_word():
    assert get_guessed_word('apple', ['a','p']) == "app__"
    assert get_guessed_word('dog',['d']) == 'd__'
    assert get_guessed_word('sleep',['s','l','e','p']) == 'sleep'
    




if __name__ == "__main__":
    # Run the test function
    test_is_guess_in_word()
    test_is_word_guessed()
    test_get_guessed_word()


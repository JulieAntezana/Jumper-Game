from word_list import list
import random

class Word:
    """
    
        init method:
            This method initializes the class with an empty list to store the users guesses to prevent repeatition
            It also initializes with a new word to be guessed for that particular round of game
    
    
        check_guess method:
            This funtion checks the user guess, it receives the letter the user guessed as an argument
                First If&else checks if the user has guessed the word before,
                    if so returns False
                
        check_letter method:      
             i      if the letter is present in the current word to be guessed:
                            returns True
                    else:
                            returns False
                            
        get_word mothod:
                    This method returns the current word to be guessed
                    
    """
    
    
    def __init__(self):
        
        self._users_guess=[]
        self._new_word = random.choice(list)
        
    def check_guess(self, letter):       
        #Tracks previous input
        if letter in self._users_guess:
            return "guessed"
        else:
            self._users_guess.append(letter)
            return
            
            
    def check_letter(self, letter):
        
        if letter in self._new_word:
            return True
        
        else:
            return False       

    def get_word(self):
        return self._new_word
from word_list import list
import random

"""
    word( **marcus
    func: new_word  
    func: check_guess(
        if right: parachute
                    display.update()
                    
    )
)
"""

class word:
    """
    
        init method:
            This method initializes the class with an empty list to store the users guesses to prevent repeatition
            It also initializes with a new word to be guessed for that particular round of game
    
    
        check_guess method:
            This funtion checks the user guess, it receives the letter the user guessed as an argument
                First If&else checks if the user has guessed the word before,
                    if so returns False
                
                
                Second If&else checks if the letters are present in the current word to be guessed
                    if present: it calls the display funtion with the letters that would be updates plus setting update to false
    """
    
    
    def __init__(self):
        
        self._users_guess=[]
        self._new_word = random.choice(list)
        
    def check_guess(self, letter):       
        #Tracks previous input
        if letter in self._users_guess:
            return False
        else:
            self._users_guess.append(letter)
            
            
        if letter in self._new_word:
            pass #call the display funtion with the letters that would be updated
        
        else:
            pass #call the display funtion setting update to false
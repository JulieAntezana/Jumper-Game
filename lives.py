class Lives:
    """
    This class handles the users lives
    
    __init__:
        This initializes the class with the number of lives
        
    subtract_lives:
        This method removes 1 from the amount of lives the user has left
        
    get_lives:
        This method gets the amount of lives left
        
    lost:
        This method checks if the amount of lives is 0, if so, the game ends 
        
        
    
    
    """
    
    def __init__(self):
        self._lives = 6       
        
    def subtract_lives(self):
        self._lives-= 1
        
    def get_lives(self):
        return self._lives
    
    def lost(self):
        if self._lives == 0:
            return True
        
        
    
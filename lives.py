class user_lives:
    
    def __init__(self):
        self._lives = 5
        
    def add(self):
        self._lives += 1
        
    def subtract(self):
        self._lives-= 1
        
    def get_lives(self):
        return self._lives
    
    def lost(self):
        if self._lives ==0:
            return True
        
        
    
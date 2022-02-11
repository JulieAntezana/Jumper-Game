
class Display:
    """
    The display class will display the letters that are guessed
    
    __init__:
        Attributes needed:
            current word converted to list
            tiles
            
    make_tiles:
        This method makes the tiles displayed on the screen based on the amount of letters presesent in the word
        
    show_tiles:
        This method prints out the tiles at whatever state it is at the moment
        
    update_tiles:
        This method replaces the guessed letter in the tiles if present in the word. it also takes note if the letter appears multiple times
        
    won:
        This method checks if the game is won by checking if there are any tiles left to complete, if none then it returns True
    
    """
    
    def __init__ (self, word):
        self._word = word
        self._word_list = list(self._word)
        self._tiles = []

    def make_tiles(self):
        for i in self._word:
            self._tiles.append("_")
            
    def show_tiles(self):       
        print("  ".join(self._tiles))
        
    def update_tiles(self, letter):
        
        
        index = 0
        for i in self._word_list:
            if i == letter.lower():
                
                self._tiles[index] = letter
                index += 1
            else:
                index += 1
                
    def won(self):
        count = 0
        for i in self._tiles:
            if i == "_":
                count += 1
        
        if count == 0:
            return True
        else:
            return False         


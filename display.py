'''
This is The file I will use '''



class Display:
    """
    The display class will display the letters that are guessed
    
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
        
    def update(self, letter):
        
        
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


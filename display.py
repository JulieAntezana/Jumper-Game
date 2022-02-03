'''
This is The file I will use '''



class Display:
    """
    The display class will display the letters that are guessed
    
    """
    
    def __init__ (self):
        self.word = "umbrella"
        self.word_list = list(self.word)
        self.tiles = []

    def make_tiles(self):
        for i in self.word:
            self.tiles.append("_")
            
    def show(self):       
        print("  ".join(self.tiles))
        
    def update(self, letter):
        
        if letter in self.word_list:
            index = 0
            for i in self.word_list:
                if i == letter.lower():
                    
                    self.tiles[index] = letter
                    index += 1
                else:
                    index += 1
                    
                    
            
        else:
            print("failed attempt")
            

        

def main():
    display =Display()
    display.make_tiles()
    display.show()
    is_game = True
    while is_game:
        user = input("Make a guess: ")
        display.update(user)
        display.show()
    
if __name__ == "__main__":
    main()

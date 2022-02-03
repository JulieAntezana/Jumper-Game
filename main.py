from display import Display
from parachute import Parachute
from words import Word

"""
parachutes(5 wrong gueses) **Julie
    returns an image either wrong or right
    
word( **marcus
    func: new_word  
    func: check_guess(
        if right: parachute
                    display.update()
                    
    )
)
display( **Rune
    func: word_tiles(get lenght of new word to create the tiles)
    func: word_display(
        display parachute and the current_word tiles
    )
    func: update
)
jumper( **lucas
    score = 5
    while loop
    func: display
    input
    func: check_guess
    
)

Dylan to arrange into files


"""
class Director:
     
    def __init__ (self):
        self.word = Word()
        self.current_word = self.word.get_word()
        self.is_playing = True
        self.display = Display(self.current_word)
        self.parachute = Parachute()
        self.lives = 4
        
    def start_game(self):
        while self.is_playing:
            self.parachute.display_parachute(self.lives)
            self.display.make_tiles()
            self.display.display()
            self.check_letter = self.word.check_guess(self.user_input())\
            
            while self.check_letter == "guessed":
                print("You already guessed that letter")
                self.check_letter = self.word.check_guess(self.user_input())

    def correct_guess(self):
        if self.check_letter:
            self.display()

    def user_input(self):
        self.guess = input("Guess a letter [a-z]: ")
        return self.guess

        


def main():
    pass

if __name__ == "__main__":
    main()
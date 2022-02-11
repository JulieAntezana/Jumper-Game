from display import Display
from parachute import Parachute
from words import Word
from lives import  user_lives
import os
from art import logo


class Director:
    """
    This is the diirector class that handles the game control and communincates with the other classes.
    
    __init__:
        This method creates objects from the other classes and call the necessary methods to begin the game
        
    start_game:
        1. This method starts a loop that keeps running unitll tiles are completed or lives are finished
        2. Makes sure the user doesnt guess one letter twice using another while loop.
        
    correct_guess:
        This method checks:
        1. if letter is correct, it calls for an update to tiles and checks if tiles are complete so the game can end
        2. if letter is wrong, it deducts lives and then make display of relevant data
        
    play_again:
        This method checks:
        1. if user wants to play again, it starts the game all over
            else:
                send a goodbye message to the terminal
                
    user_input:
        This method takes an input from the user and returns it
    
    """
     
    def __init__ (self):
        self.word = Word()
        self.current_word = self.word.get_word()
        self.is_playing = True
        self.display = Display(self.current_word)
        self.parachute = Parachute()
        self.lives = user_lives()
        self.parachute.show_parachute(self.lives.get_lives())
        self.display.make_tiles()
        self.display.show_tiles()
        print()
        self.letter = ""
        
    def start_game(self):
        while self.is_playing:

            self.guessed = self.word.check_guess(self.user_input())
            
            while self.guessed == "guessed":
                print("You already guessed that letter")
                self.guessed = self.word.check_guess(self.user_input())
            
            
            self.check_letter = self.word.check_letter(self.letter)
            
            
            self.correct_guess()
                

    def correct_guess(self):
        
        if self.check_letter:
            
            self.display.update_tiles(self.letter)
            self.display.show_tiles()
    
            self.parachute.show_parachute(self.lives.get_lives())
            if self.display.won():
                self.is_playing = False
                print("Yay! you won")
                self.play_again()
                
            
            
        else:
            self.display.show_tiles()
            
            self.lives.subtract_lives()
            
            self.parachute.show_parachute(self.lives.get_lives())
            if self.lives.lost():
                print("The word is", self.current_word.upper())
                self.is_playing = False
                self.play_again()
                
    
    def play_again(self):
        print()
        options = ["y","n"]
        ask_user = input("Do you want to play again? (y/n): ").lower()
        while ask_user not in options:
            print("Invalid entry, try again")
            ask_user = input("Do you want to play again? (y/n): ")
            
        if ask_user == "y":
            os.system('cls||clear')
            main()
        else:
            print("Thanks for playing, Hope to see you soon")
            print()        
            return
            
            
            
            

    def user_input(self):
        self.guess = input("Guess a letter [a-z]: ")
        self.letter = self.guess
        return self.guess

        


def main():
    """Tis funtion starts the game play  using try to catch relevant errors
    """
    try:
        print(logo)
        game = Director()
        game.start_game()
        
    #catch the ValueError type 
    except ValueError as value_err:
        print(type(value_err).__name__, value_err, sep=": ")
        print(f"This {value_err} is not a valid input, \
            \nplease run the program again and try a valid number")    
        
    
    # catch the filenotfounderror type
    except FileNotFoundError as not_found_err:
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file  does not exist in this directory \
            \nRun the program again using a file name that exists")
        
    # catch the permissionerror type    
    except PermissionError as perm_err:
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You do not have permission to open the file \
            \nPlease run the program again and use a file within your permission rights")    

if __name__ == "__main__":
    main()
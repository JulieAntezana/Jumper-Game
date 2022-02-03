'''
This is The file I will use '''
# from words import new_word
import test


def main():
    hilo = Display().display()
    # os.system('cls||clear')
    # print(logo)
    # hilo
    l = Display().guessed_letters()
    # l
    # hilo.display()

class Display:
    """
    The display class will display the letters that are guessed
    
    """
    
    def __init__ (self, word):
        self.word = word
        # self.tiles = ""

    # def make_tiles(self):
        # letters = "four"
        # guess = "o"
        # for letter in self.word:
        #     self.tiles += "_ "
        
            
    # def display(self):
    #     print(self.tiles)

    def display(self, letter, update = False):
        
        # if not update:
        #     self.display()
        # else:

        for i in self.word:
            if i == letter:
                print (letter, end =" ")
            else:
                print ("_", end =" ")


    def guessed_letters(self):
        gletters=[]
        gletter = input("type letter :")
        gletters.append(gletter)
        print(gletters)

if __name__ == "__main__":
    main()
#         pass

#     def display(guessedLetters):
#         pass
#         # print(_users_guess)

#     def display(parachute):
#         pass

# from itertools import count


# lettercount = 4 #Four



# letters = "four"
# guess = "o"
# # length.letters

# for letter in letters:
#     if guess in letter:
#         print (letter, end =" ")
#     else:
#         print ("_", end =" ")
        



# for letter in lettercount:
#     print (" _", end =" ")

# print(letters[1])


# i = 1
# while i < 6:
#   print("_", end =" ")
#   i += 1
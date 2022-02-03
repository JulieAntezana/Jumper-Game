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
    
    def display(letters):
        letters = "four"
        guess = "o"
        for letter in letters:
            if guess in letter:
                print (letter, end =" ")
            else:
                print ("_", end =" ") 
        print("The end")
    
        

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
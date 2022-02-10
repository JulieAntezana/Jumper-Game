class Parachute:
    # This class has the responsibility to provide a series of parachute
    # images for game.
    # There will be an image of a full parachute to begin the game.
    # There will be four other images depicting the skydiver minus parachute parts.
    # The final image will be the skydiver with no parachute to end the game.
    # The images are contained within an array called stages.

    def __init__(self):
        # Class constructor
        self.lives_remaining = 4
    # #     self.display.update = False

    def get_is_correct(self):
        display = Display()
        is_correct = self.display.get_is_correct()
        if is_correct == False:
            return is_correct == False

    def parachute_update(self, update):
        lives_remaining = []
        self.display.get_is_correct()
        lives_remaining = self.parachute_stages(lives_remaining)
        if self.display.get_is_correct:
            lives_remaining -= 1

        return lives_remaining

    # def display_parachute(lives_remaining):
    #     print(self.parachute_stages(lives_remaining))

    def parachute_stages():

        # An image can be called into the program using the parachute_stage method with
        # the parameter of an index number for the number of tries remaining.
        # For example: self.parachute_stage(stages[4]) will return the last image in the array,
        # which is the full parachute with four tries remaining. When there are zero tries
        # remaining, the program would call for self.parachute_stage(stages[0]) which would
        # return the skydiver with no parachute to end the game.

        stages = ["""
  X
 /|\\
 / \\
""",
                  """"
 \\ /
  0
 /|\\
 / \\
/___\\
""",
                  """"
\\   /
 \\ /
  0
 /|\\
 / \\
""",
                  """"
/___\\
\\   /
 \\ /
  0
 /|\\
 / \\
""",
                  """"
 ___
/___\\
\\   /
 \\ /
  0
 /|\\
 / \\
"""
                  ]

        lives_remaining = 4
        stages.__getitem__(lives_remaining)
        print(stages.__getitem__(lives_remaining))

        # return self.stages[lives_remaining]

    # def __init__(self):
    #     self.parachute = self.stages[4]

    # def draw(self, lives_remaining):
    #     self.parachute = self.stages[lives_remaining]
    #     print(self.parachute)


class Display:
    """
    The display class will display the letters that are guessed

    """

    def __init__(self):
        self.word = "umbrella"
        self.word_list = list(self.word)
        self.tiles = []
        self.parachute = Parachute()
        lives_remaining = 4

    def make_tiles(self):
        for i in self.word:
            self.tiles.append("_")

    def show(self):
        print("  ".join(self.tiles))

    def update(self, letter):

        if letter in self.word_list:
            index = 0
            is_correct = True
            for i in self.word_list:

                if i == letter.lower():

                    self.tiles[index] = letter
                    index += 1
                else:
                    index += 1
        else:
            print("failed attempt")
            is_correct = False

    def get_is_correct(self, update):
        """Whether or not the letter has been guessed correctly.

        Args:
            self (Display): An instance of Display.

        Returns:
            boolean: True if the letter was guessed correctly; false if otherwise.
        """
        if update.is_correct == False:

            return False


def main():
    display = Display()
    parachute = Parachute
    display.make_tiles()
    display.show()
    lives_remaining = 4
    is_game = True
    while is_game:
        user = input("Make a guess: ")
        display.update(user)
        display.show()
        parachute.parachute_stages()


if __name__ == "__main__":
    main()

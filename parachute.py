class parachute:
    # This class has the responsibility to provide a series of parachute
    # images for game.
    # There will be an image of a full parachute to begin the game.
    # There will be four other images depicting the skydiver minus parachute parts.
    # The final image will be the skydiver with no parachute to end the game.
    # The images are contained within an array called stages.

    def __init__(self):

        self.stages = []

    def parachute_stage(tries):
        # An image can be called into the program using the parachute_display method with
        # the parameter of an index number for the number of tries remaining.
        # For example: self.parachute_stage(stages[4]) will return the first image in the array,
        # which is the full parachute with four tries remaining. When there are zero tries
        # remaining, the program would call for s.paachute_stage([0]) which would
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
        return stages[tries]

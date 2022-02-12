
class Parachute:
    # This class has the responsibility to provide a series of parachute
    # images for game.
    # The images are contained within an array, or list, called stages.

    def __init__(self):
        # This method creates an instance of the class, which is a list of 
        # parachute images.
        self._stages = []

    def get_parachute(self, lives):
        # This method displays the appropriate parachute, as determined by the 
        # lives parameter.
        print(self.parachute_stage()[lives])

    def parachute_stage(self):
        # This method holds the parachute images 

        self._stages = ["""
  X
 /|\\
 / \\
 
^^^^^
""",
                  """
 \\ /
  0
 /|\\
 / \\

^^^^^
""",
                  """
 ___
 \\ /
  0
 /|\\
 / \\

^^^^^
""",
                  """
\\___/
 \\ /
  0
 /|\\
 / \\

^^^^^
""",
                  """
 ___
\\___/
 \\ /
  0
 /|\\
 / \\

^^^^^
""",
                  """
/___\\
\\___/
 \\ /
  0
 /|\\
 / \\

^^^^^
""",
                  """
 ___
/___\\
\\___/
 \\ /
  0
 /|\\
 / \\

^^^^^
"""
                  ]
        
        return self._stages
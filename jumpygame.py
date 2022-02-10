import pygame as pg
import sys
from pygame.locals import *
import time
import math
import random
from word_list import list

# setup display
pg.init()
WIDTH, HEIGHT = 800, 500
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Jumper")

# button variables
RADIUS = 23
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 97
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pg.font.SysFont('arial', 40)
WORD_FONT = pg.font.SysFont('arial', 60)
TITLE_FONT = pg.font.SysFont('arial', 70)

# load images
images = []
for i in range(6):
    image = pg.image.load("images/jumper" + str(i) + ".png")
    images.append(image)


# game variables
    jumper_status = 5
    word = random.choice(list)
    guessed = []
    won = False


# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def opening():
    display_message(
        """JUMPER (click to start)""")


def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("JUMPER", 1, BLACK)
    win.blit(text, (WIDTH / 2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pg.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() /
                     2, y - text.get_height() / 2))

    win.blit(images[jumper_status], (150, 100))
    pg.display.update()


def display_message(message):
    pg.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width() /
             2, HEIGHT/2 - text.get_height()/2))
    pg.display.update()
    pg.time.delay(1000)


def real_word(word):
    text = WORD_FONT.render(word, 1, BLACK)
    win.blit(text, (450, 150))
    pg.display.update()
    pg.time.delay(1000)


def main():
    global jumper_status

    FPS = 60
    clock = pg.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                m_x, m_y = pg.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                jumper_status -= 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("You WON!")
            reset
            break

        if jumper_status == 0:
            real_word(word)
            display_message("You LOST!")
            reset_game()


def reset_game():
    jumper_status = 5
    word = random.choice(list)
    guessed = []
    won = False
    opening()

# run the game loop forever
while True:
    opening()
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # the user clicked; start the game

            main()

            if(won or jumper_status == 0):
                reset_game()

    pg.display.update()

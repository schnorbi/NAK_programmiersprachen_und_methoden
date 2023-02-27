import pgzrun
from random import randint

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        place_apple()
    else:
        print("Game Over")
        quit()

apple = Actor('apple')
place_apple()
pgzrun.go()
import pgzrun
import math

PIX = 100
G = 9.81
V = 5
DEG = 45
T = 0

X = 10
Y = 400

def draw():
    screen.clear()
    apple.draw()

def apple_place():
    apple.x = X
    apple.y = Y

def step():
    global V, DEG, X, Y, T

    if Y > 800:
        quit()

    else:
        T = T + (1/300)

        X = X + (V*T*math.cos(math.radians(DEG)))*100
        Y = Y - (V*T*math.sin(math.radians(DEG))*-(G/2)*T**2)*100

        apple_place()

apple = Actor('apple')
apple_place()
clock.schedule_interval(step, 1/300)
pgzrun.go()

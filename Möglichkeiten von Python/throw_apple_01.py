import pgzrun

PIX = 100
G = 9.81
V_X = 4
V_Y = 8

X = 10
Y = 400

def draw():
    screen.clear()
    apple.draw()

def apple_place():
    apple.x = X
    apple.y = Y

def step():
    global V_Y, X, Y

    if Y > 800:
        quit()

    else:
        X = X + (V_X*(1/300))*100
        Y = Y - (V_Y*(1/300))*100

        V_Y = V_Y - G*(1/300)

        apple_place()

apple = Actor('apple')
apple_place()
clock.schedule_interval(step, 1/300)
pgzrun.go()

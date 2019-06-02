

import pygame
import gamebox
import random

camera = gamebox.Camera(600, 600)
show_splash = True
ticks = 0

pillars = [
    gamebox.from_color(0, -350, 'brown', 50, 1200),
    gamebox.from_color(300, -350, 'brown', 50, 1200),
    gamebox.from_color(600, -350, 'brown', 50, 1200),
    gamebox.from_color(900, -350, 'brown', 50, 1200),
]

pillars_2 = [
    gamebox.from_color(0, 950, 'brown', 50, 1200),
    gamebox.from_color(300, 950, 'brown', 50, 1200),
    gamebox.from_color(600, 950, 'brown', 50, 1200),
    gamebox.from_color(900, 950, 'brown', 50, 1200),
]

floor = gamebox.from_color(300, 600, 'white', 600, 10)

bird = gamebox.from_color(50, 300, 'gray', 20, 20)


def splash(keys):
    global show_splash
    camera.clear('grey')
    camera.draw(gamebox.from_text(camera.x, camera.y, "Thank You For Choosing FINNAIR", "Arial", 30, "red"))
    camera.draw(gamebox.from_text(camera.x, camera.y+50, "(press space to begin your journey)", "Arial", 15, "white"))
    if pygame.K_SPACE in keys:
        show_splash = False
    camera.display()


def tick(keys):
    global ticks
    ticks += 1
    if show_splash:
        splash(keys)
        return

    camera.clear('cyan')

    time = gamebox.from_text(0, 0, str(ticks//30), "Times New Roman", 30, "red")
    time.top = camera.top
    time.right = camera.right
    camera.draw(time)

    r = random.randrange(-80, 80)
    for pillar in pillars:
        camera.draw(pillar)
        pillar.x -= 8
        if pillar.right < camera.left:
            pillar.x += 1200
            pillar.y -= r

    for pillar in pillars_2:
        camera.draw(pillar)
        pillar.x -= 8
        if pillar.right < camera.left:
            pillar.x += 1200
            pillar.y -= r

    if pygame.K_SPACE in keys:
        bird.speedy = -8

    if bird.touches(floor, 15):
        gamebox.pause()
        camera.draw(gamebox.from_text(camera.x, camera.y, "Your score is " + str(ticks//30), "Arial", 30, "red"))

    for pillar in pillars:
        if bird.right_touches(pillar, -5) or bird.top_touches(pillar, 2):
            gamebox.pause()
            camera.draw(gamebox.from_text(camera.x, camera.y, "Your score is " + str(ticks//30), "Arial", 30, "red"))

    for pillar in pillars_2:
        if bird.right_touches(pillar, -5) or bird.bottom_touches(pillar, 2):
            gamebox.pause()
            camera.draw(gamebox.from_text(camera.x, camera.y, "Your score is " + str(ticks//30), "Arial", 30, "red"))

    bird.speedy *= .9
    bird.speedy += .9

    bird.move_speed()
    camera.draw(bird)
    camera.draw(floor)
    camera.display()

gamebox.timer_loop(1000, tick)

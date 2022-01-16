import sys

import pygame
pygame.init()

width, height = 800, 600
fps = 60

window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

shrift = pygame.font.Font(None, 35)
shrift1 = pygame.font.Font(None, 80)

city = pygame.image.load('city.jpg')
vert = pygame.image.load('berd.png')
startscreen = pygame.image.load("start.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False

    window.blit(startscreen, (0, 0))
    pygame.display.update()

pos, speed, uskor = height // 2, 0, 0
chel = pygame.Rect(width // 3, pos, 34, 24)


nacal = 'start'
vrem = 60
ani = 0

trub = []
fon = []

fon.append(pygame.Rect(0, 0, 288, 600))

live = 3
ochko = 0

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    press = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    click = press[0] or keys[pygame.K_SPACE]

    if vrem > 0:
        vrem -= 1

    ani = (ani + 0.2) % 4

    for i in range(len(fon)-1, -1, -1):
        fo = fon[i]
        fo.x -= 1

        if fo.right < 0:
            fon.remove(fo)

        if fon[len(fon)-1].right <= width:
            fon.append(pygame.Rect(fon[len(fon)-1].right, 0, 288, 600))


    for i in range(len(trub)-1, -1, -1):
        tru = trub[i]
        tru.x -= 3

        if tru.right < 0:
            trub.remove(tru)

    if nacal == 'start':
        if click and vrem == 0 and len(trub) == 0:
            nacal = 'play'

        pos += (height // 2 - pos) * 0.1
        chel.y = pos
    elif nacal == 'play':
        if click:
            uskor = -3
        else:
            uskor = 0

        pos += speed
        speed = (speed + uskor + 1) * 0.7
        chel.y = pos

        if len(trub) == 0 or trub[len(trub)-1].x < width - 500:
            trub.append(pygame.Rect(width, 0, 50, 200))
            trub.append(pygame.Rect(width, 400, 50, 200))
        if chel.top < 0 or chel.bottom > height:
            nacal = 'fall'
        if live == 0:
            nacal = 'over'

        if nacal == 'play':
            ochko += 0.06

        for tru in trub:
            if chel.colliderect(tru):
                nacal = 'fall'

    elif nacal == 'fall':
        nacal = 'start'
        speed = 0
        uskor = 0
        vrem = 60
        live -= 1


    elif nacal == 'over':
        ochko = 0
        nacal = 'start'
        speed = 0
        uskor = 0
        vrem = 60
        live = 3




    window.fill(pygame.Color('black'))
    for fo in fon:
        window.blit(city, fo)


    for tru in trub:
        pygame.draw.rect(window, pygame.Color('red'), tru)

    image = vert.subsurface(34 * int(ani), 0, 34, 24)
    window.blit(image, chel)

    pis = shrift.render('Очки:' + str(int(ochko)), 0, pygame.Color('black'))
    window.blit(pis, (10, 10))

    pis = shrift.render('Жизни:' + str(live), 0, pygame.Color('black'))
    window.blit(pis, (10, height - 30))

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
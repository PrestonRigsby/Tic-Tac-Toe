from tabnanny import check
from settings import *
from functions import *

pygame.init()
clock = pygame.time.Clock()

play = True

tilemap = [[0, 0, 0], 
           [0, 0, 0], 
           [0, 0, 0]]

xtiles = []
otiles = []

X = pygame.image.load("../Python/Tic Tac Toe/X (2).png")
X = pygame.transform.scale(X, (200, 200))
O = pygame.image.load("../Python/Tic Tac Toe/O.png")
O = pygame.transform.scale(O, (200, 200))

w = pygame.image.load("../Python/Tic Tac Toe/white.jpg")
pygame.display.set_icon(w)

turn = 1

boxes = []

boxSurface = pygame.Surface((200, 200))
box = boxSurface.get_rect()
boxes.append(boxSurface)

#---PLAY LOOP---#
while play:
    clock.tick(60)

    mpos = pygame.mouse.get_pos()

    tileposx = mpos[0]//200
    tileposy = mpos[1]//200

    box.topleft = (tileposx*200, tileposy*200)

    if turn == 1:
        pygame.display.set_icon(X)
        pygame.display.set_caption("X's turn")
    elif turn == 2:
        pygame.display.set_icon(O)
        pygame.display.set_caption("O's turn")
    else:
        pygame.display.set_caption("Tic Tac Toe")

    for y in range(3):
        for x in range(3):
            if tilemap[y][x] == 1:
                screen.blit(X, (x*200, y*200))
            if tilemap[y][x] == 2:
                screen.blit(O, (x*200, y*200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if tilemap[tileposy][tileposx] == 0:   
                tilemap[tileposy][tileposx] = turn
                if turn == 1:
                    xtiles.append([tileposx, tileposy])
                    turn = 2
                elif turn == 2:
                    otiles.append([tileposx, tileposy])
                    turn = 1
            print(tilemap[0])
            print(tilemap[1])
            print(tilemap[2])
            print(" ")

    if checkWin(xtiles):
        print("-----------------------")
        print("X Won!")
        play = False
    if checkWin(otiles):
        print("-----------------------")
        print("O Won!")
        play = False

    screen.blit(boxSurface, box)

    pygame.display.update()

    screen.fill(screen_color)
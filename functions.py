from settings import *

def makeText(font, size, text, location, color):
    f = pygame.font.SysFont(font, size, True)
    sText = f.render(text, True, color)
    rText = sText.get_rect(topleft = location)
    return sText, rText

def checkWin(tiles):
    win1 = [[0, 0], [1, 0], [2, 0]]
    win2 = [[0, 1], [1, 1], [2, 1]]
    win3 = [[0, 2], [1, 2], [2, 2]]
    win4 = [[0, 0], [0, 1], [0, 2]]
    win5 = [[1, 0], [1, 1], [1, 2]]
    win6 = [[2, 0], [2, 1], [2, 2]]
    win7 = [[0, 0], [1, 1], [2, 2]]
    win8 = [[0, 2], [1, 1], [2, 0]]

    if win1[0] in tiles and win1[1] in tiles and win1[2] in tiles:
        return True
    elif win2[0] in tiles and win2[1] in tiles and win2[2] in tiles:
        return True
    elif win3[0] in tiles and win3[1] in tiles and win3[2] in tiles:
        return True
    elif win4[0] in tiles and win4[1] in tiles and win4[2] in tiles:
        return True
    elif win5[0] in tiles and win5[1] in tiles and win5[2] in tiles:
        return True
    elif win6[0] in tiles and win6[1] in tiles and win6[2] in tiles:
        return True
    elif win7[0] in tiles and win7[1] in tiles and win7[2] in tiles:
        return True
    elif win8[0] in tiles and win8[1] in tiles and win8[2] in tiles:
        return True
    else:
        return False

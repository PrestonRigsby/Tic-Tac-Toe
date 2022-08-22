import pygame

colors = {
"black" : (0, 0, 0),
"white" : (255, 255, 255),
"red" : (255, 0, 0),
"green" : (0, 255, 0),
"blue" : (0, 0, 255),
"yellow" : (255, 255, 0)
}

#---SCREEN---#
screen_size = (600, 600)
screen_color = colors["white"]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tic Tac Toe")
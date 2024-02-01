# William Castengera, 2/1/24, v0.0
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

Sky_Surface = pygame.image.load('img/ultPygame/Sky_Image.png')
Ground_Surface = pygame.image.load('img/ultPygame/Ground_Image.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(Sky_Surface, (0,0))
    screen.blit(Ground_Surface, (0,300))

    pygame.display.update()
    clock.tick(60)
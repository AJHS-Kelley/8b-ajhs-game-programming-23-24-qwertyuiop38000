# William Castengera, 2/1/24, v0.0
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

test_surface = pygame.image.load('img/Downloads/OneDrive - Duval County Public Schools/8b-ajhs-game-programming-23-24-qwertyuiop38000/08_ultimateIntroPygame/Sky_Image.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (0,0))

    pygame.display.update()
    clock.tick(60)
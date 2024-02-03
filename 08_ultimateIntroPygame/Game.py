# William Castengera, 2/1/24, v0.0
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

Sky_Surface = pygame.image.load('img/ultPygame/Sky_Image.jpg')
Ground_Surface = pygame.image.load('img/ultPygame/Ground_Image.png')
text_Surface = test_font.render('My game', False, 'Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(Sky_Surface, (0,0))
    screen.blit(Ground_Surface, (0,311))
    screen.blit(text_Surface, (350,100))

    pygame.display.update()
    clock.tick(60)
# William Castengera, 2/1/24, v0.0
import pygame
from sys import exit

# You are  a little behind, please get finished.  You may need to work outside of class to complete it on time. 


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('08_ultimateIntroPygame/ultPygame/font/Pixeltype.ttf', 50)

Sky_Surface = pygame.image.load('img/ultPygame/Sky_Image.jpg').convert_alpha()
Ground_Surface = pygame.image.load('img/ultPygame/Ground_Image.png').convert_alpha()
Text_Surface = test_font.render('My game', False, 'Black')
Character_surface = pygame.image.load('img/ultPygame/Pacman_Image.png').convert_alpha()
Character_x_Position = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    Character_x_Position -= 4
    if Character_x_Position > 800:
        Character_x_Position = 0
    if Character_x_Position < 0:
        Character_x_Position = 800
    screen.blit(Sky_Surface, (0,0))
    screen.blit(Ground_Surface, (0,311))
    screen.blit(Text_Surface, (350,100))
    screen.blit(Character_surface, (Character_x_Position,300))


    pygame.display.update()
    clock.tick(60)
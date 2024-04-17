# Final Project, William Castengera, v0.0
import sys, random, pygame

resolution = 0 # O = Low Resolution, 1 = High Resolution

difficulty = int(input("Please choose a difficulty. Enter 1 for easy or 2 for hard.\n"))
if difficulty == 0:
    pygame.display.set_caption('Maze Of Doom -- Easy')
else:
    pygame.display.set_caption('Maze Of Doom -- Hard')
pygame.init()
clock = pygame.time.Clock()
if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080
screen = pygame.display.set_mode((x, y))
z = 680
c = 550
Maze_Surface = pygame.image.load('img/imagesX_800x600.png').convert_alpha()
character_surface = pygame.image.load('img/character.png').convert_alpha()


while True:
    character = character_surface.get_rect(topleft = (z,c))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(Maze_Surface, (0,0))
    screen.blit(character_surface, character)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        c -= 5
    if keys[pygame.K_a]:
        z -= 5
    if keys[pygame.K_d]:
        z += 5
    if keys[pygame.K_s]:
        c += 5
    pygame.display.update()
    clock.tick(60)
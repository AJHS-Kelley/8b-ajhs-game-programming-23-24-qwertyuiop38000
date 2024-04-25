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
test_surface = pygame.image.load('img/41509588-16212fda-721c-11e8-8650-dc1cdd619072.png').convert_alpha()
game_active = False
open_screen_surface = pygame.image.load('img/')

while True:
    character = character_surface.get_rect(topleft = (z,c))
    test_rect = test_surface.get_rect(topleft = (100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if game_active:
        screen.blit(Maze_Surface, (0,0))
        screen.blit(character_surface, character)
        screen.blit(test_surface, test_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_a] or keys[pygame.K_LEFT]):
                if character.colliderect(test_rect):
                    z += 5
                    continue
                else:
                    c -= 5
                    z -= 5
            elif (keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
                if character.colliderect(test_rect):
                    z -= 5
                    continue
                else:
                    c -= 5
                    z += 5
            elif character.colliderect(test_rect):
                c += 5
            else:
                c -= 5
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if character.colliderect(test_rect):
                z += 5
                continue
            else:
                z -= 5
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            z += 5
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            c += 5
    else:

    pygame.display.update()
    clock.tick(60)
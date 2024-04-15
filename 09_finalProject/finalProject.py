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
pos = (0,0)
Maze_Surface = pygame.image.load('img/imagesX_800x600.png').convert_alpha()
character_surface = pygame.image.load('img/character.png').convert_alpha()
character = character_surface.get_rect(topleft = (680,550))
def getCoords(self):
    return [self.pos[0], self.pos[1], self.pos[0] + self.size[0], self.pos[1] + self.size[1]]
def updatePos(self, coords):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and self.getCoords()[1]> self.minPos[1]:
        self.pos[1] -= 0.3
    if keys[pygame.K_DOWN] and self.getCoords()[3]< self.maxPos[1]:
        self.pos[1] += 0.3
    if keys[pygame.K_w] and self.getCoords()[1]> self.minPos[1]:
        self.pos[1] -= 0.3
    if keys[pygame.K_s] and self.getCoords()[3]< self.maxPos[1]:
        self.pos[1] += 0.3
def __init__(self):
    self.pos = pos
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(Maze_Surface, (0,0))
    screen.blit(character_surface, character)
    __init__(character)
    updatePos(character, getCoords(character))
    pygame.display.update()
    clock.tick(60)
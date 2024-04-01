# Final Project, William Castengera, v0.0
import sys, random, pygame

resolution = 1 # O = Low Resolution, 1 = High Resolution

difficulty = int(input("Please choose a difficulty. Enter 1 for easy or 2 for hard.\n"))
if difficulty == 1:
    pygame.display.set_caption('Maze Of Doom -- Easy')
else:
    pygame.display.set_caption('Maze Of Doom -- Hard')
pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if resolution == 0:
        x = 800
        y = 600
    else:
        x = 1920
        y = 1080
    screen = pygame.display.set_mode((x, y))

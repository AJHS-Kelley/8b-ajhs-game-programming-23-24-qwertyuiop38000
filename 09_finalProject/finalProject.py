# Final Project, William Castengera, v0.0
import sys, random, pygame

resolution = 0 # O = Low Resolution, 1 = High Resolution
logfile = open("logfile.txt", "w")
difficulty = 0
difficulty_select = False
pygame.display.set_caption('Maze Of Doom')
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
c = 165
Maze_Surface = pygame.image.load('img/shot01 (1).jpg').convert_alpha()
character_surface = pygame.image.load('img/character.png').convert_alpha()
test_surface = pygame.image.load('img/41509588-16212fda-721c-11e8-8650-dc1cdd619072.png').convert_alpha()
game_active = False
open_screen_surface = pygame.image.load('img/Title-Background-Image_800x600.png')
text_font = pygame.font.Font(None, 50)
text_font2 = pygame.font.Font(None, 50)
text_font3 = pygame.font.Font(None,75)
difficulty_select_text = text_font3.render("Choose your difficulty", False, 'Red')
hard_Choice = text_font2.render("Hard", False, 'Red')
easy_Choice = text_font2.render("Easy", False, 'Red')
hard_rect = hard_Choice.get_rect(center = (200,300))
easy_rect = easy_Choice.get_rect(center = (600,300))
text_surface = text_font.render("Welcome to the Maze of Doom", False, 'Red')
play_Button = pygame.image.load('img/play_button.png')
play_Button_Rect =  play_Button.get_rect(center = (400,300))
wall_rect2 = test_surface.get_rect(topleft = (-206,0))
while True:
    character = character_surface.get_rect(topleft = (z,c))
    wall_rect = test_surface.get_rect(bottomright = (673, 600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_Button_Rect.collidepoint(event.pos):
                game_active = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hard_rect.collidepoint(event.pos):
                difficulty_select = True
                difficulty = "hard"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if easy_rect.collidepoint(event.pos):
                difficulty_select = True
                difficulty = "easy"
        if event.type == pygame.MOUSEMOTION:
            if game_active and difficulty_select:
                logfile.write(str(event.pos) + "\n")
    if game_active:
        if difficulty_select == True:
            screen.blit(Maze_Surface, (0,0))
            screen.blit(character_surface, character)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                if (keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_a] or keys[pygame.K_LEFT]):
                    if character.colliderect(wall_rect):
                        z += 5
                        continue
                    else:
                        c -= 5
                        z -= 5
                elif (keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
                    if character.colliderect(wall_rect):
                        z -= 5
                        continue
                    else:
                        c -= 5
                        z += 5
                else:
                    c -= 5
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if character.colliderect(wall_rect):
                    z += 5
                else:
                    z -= 5
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                z += 5
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                c += 5
        else:
            screen.blit(open_screen_surface, (0,0))
            screen.blit(difficulty_select_text, (125,25))
            screen.blit(hard_Choice, hard_rect)
            screen.blit(easy_Choice, easy_rect)
    else:
        screen.blit(open_screen_surface, (0,0))
        screen.blit(text_surface, (150,25))
        screen.blit(play_Button, play_Button_Rect)   
    pygame.display.update()
    clock.tick(60)
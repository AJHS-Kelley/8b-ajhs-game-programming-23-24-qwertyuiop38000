import pygame
pygame.init()
def updatePos(self):
    keys = pygame.key.get_pressed()
    if self.player == 1:
        if keys[pygame.K_UP] and self.getCoords()[1]> self.minPos[1]:
                self.pos[1] -= 0.3
        if keys[pygame.K_DOWN] and self.getCoords()[3]< self.maxPos[1]:
                self.pos[1] += 0.3
    else:
        if keys[pygame.K_w] and self.getCoords()[1]> self.minPos[1]:
                self.pos[1] -= 0.3
        if keys[pygame.K_s] and self.getCoords()[3]< self.maxPos[1]:
                self.pos[1] += 0.3
updatePos()
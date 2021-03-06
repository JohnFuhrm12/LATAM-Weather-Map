import pygame
import os

# Button Image
STAR = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "star.png")), (30, 30))

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.hover = False

    def draw(self, surface):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # If hovering over button do something
        if self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "star2.png")), (30, 30))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if not self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "star.png")), (30, 30))

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
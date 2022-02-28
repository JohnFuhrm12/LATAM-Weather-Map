import pygame

WIDTH, HEIGHT = 500, 700  # Game window dimensions
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Makes app window
class button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # If hovering over button do something
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        WIN.blit(self.image, (self.rect.x, self.rect.y))
        return action
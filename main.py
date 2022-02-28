import pygame
import button
import buenosaires
import os
pygame.font.init()

# Tests
print("Temp:", buenosaires.temp)
print(buenosaires.time.capitalize())
print(buenosaires.sky.title())

WIDTH, HEIGHT = 500, 700  # Game window dimensions
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Makes app window
pygame.display.set_caption("LATAM Climate Map")  # Sets name of app window
programIcon = pygame.image.load(
    os.path.join("Assets", "weathericon.png"))
pygame.display.set_icon(programIcon)

# Menu background image
BACKGROUND_MAP = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "latam.png")), (WIDTH, HEIGHT))

# RGB Colors
WHITE = (255, 255, 255)

# Draws app window
def draw_window():
    WIN.blit(BACKGROUND_MAP, (0, 0))

# Button image
DOT = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "dot.png")), (20, 20))

# Button locations
BA = button.button(240, 470, DOT)
BOGOTA = button.button(80, 80, DOT)
BRASILIA = button.button(340, 270, DOT)

# Keeps the app window open until user quits
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # Do something when button is clicked
            if BA.draw():
                buenosaires.draw_ba_window()
            if BOGOTA.draw():
                print("BOG")
            if BRASILIA.draw():
                print("BRA")

            draw_window()
            BA.draw()
            BOGOTA.draw()
            BRASILIA.draw()

        pygame.display.update()


main()

import pygame
import button
import os

import buenosaires
import bogota
import brasilia

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

# Button locations
BA = button.Button(240, 470, button.DOT)
BOGOTA = button.Button(80, 80, button.DOT)
BRASILIA = button.Button(340, 270, button.DOT)

# Keeps the app window open until user quits
def main_menu():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        WIN.blit(BACKGROUND_MAP, (0, 0))
        BA.draw(WIN)
        BOGOTA.draw(WIN)
        BRASILIA.draw(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if BA.draw(WIN):
            ba_screen()
        if BOGOTA.draw(WIN):
            bog_screen()
        if BRASILIA.draw(WIN):
            bra_screen()

        pygame.display.update()

# Separate Game Loops for City Screens

# Buenos Aires
def ba_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        buenosaires.draw_ba_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            pygame.display.update()

# Bogota
def bog_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        bogota.draw_bog_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            pygame.display.update()

# Brasilia
def bra_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        brasilia.draw_bra_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            pygame.display.update()

main_menu()

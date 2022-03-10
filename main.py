import pygame
import cap_button
import button
import sys
import os

import buenosaires
import bogota
import brasilia
import rio
import lima
import santiago
import caracas
import lapaz
import asuncion
import quito
import montevideo
import cusco
import manaus
import bariloche

pygame.init()

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
BA = cap_button.Button(235, 465, cap_button.STAR)
BOGOTA = cap_button.Button(80, 80, cap_button.STAR)
BRASILIA = cap_button.Button(340, 270, cap_button.STAR)
LIMA = cap_button.Button(45, 240, cap_button.STAR)
SANTIAGO = cap_button.Button(120, 440, cap_button.STAR)
CARACAS = cap_button.Button(145, 20, cap_button.STAR)
LAPAZ = cap_button.Button(135, 286, cap_button.STAR)
ASUNCION = cap_button.Button(245, 365, cap_button.STAR)
QUITO = cap_button.Button(30, 125, cap_button.STAR)
MONTEVIDEO = cap_button.Button(260, 460, cap_button.STAR)
RIO = button.Button(375, 360, button.DOT)
CUSCO = button.Button(105, 260, button.DOT)
MANAUS = button.Button(220, 160, button.DOT)
BARILOCHE = button.Button(135, 530, button.DOT)


# Keeps the app window open until user quits
def main_menu():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        WIN.blit(BACKGROUND_MAP, (0, 0))
        BA.draw(WIN)
        BOGOTA.draw(WIN)
        BRASILIA.draw(WIN)
        RIO.draw(WIN)
        LIMA.draw(WIN)
        SANTIAGO.draw(WIN)
        CARACAS.draw(WIN)
        LAPAZ.draw(WIN)
        ASUNCION.draw(WIN)
        QUITO.draw(WIN)
        MONTEVIDEO.draw(WIN)
        CUSCO.draw(WIN)
        MANAUS.draw(WIN)
        BARILOCHE.draw(WIN)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        if BA.draw(WIN):
            ba_screen()
        if BOGOTA.draw(WIN):
            bog_screen()
        if BRASILIA.draw(WIN):
            bra_screen()
        if RIO.draw(WIN):
            rio_screen()
        if LIMA.draw(WIN):
            lima_screen()
        if SANTIAGO.draw(WIN):
            santiago_screen()
        if CARACAS.draw(WIN):
            caracas_screen()
        if LAPAZ.draw(WIN):
            lapaz_screen()
        if ASUNCION.draw(WIN):
            asuncion_screen()
        if QUITO.draw(WIN):
            quito_screen()
        if MONTEVIDEO.draw(WIN):
            mont_screen()
        if CUSCO.draw(WIN):
            cusco_screen()
        if MANAUS.draw(WIN):
            manaus_screen()
        if BARILOCHE.draw(WIN):
            barilo_screen()


# Separate Game Loops for City Screens

# Buenos Aires
def ba_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        buenosaires.draw_ba_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# Bogota
def bog_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        bogota.draw_bog_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# Brasilia
def bra_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        brasilia.draw_bra_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# Rio
def rio_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        rio.draw_rio_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# Lima
def lima_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        lima.draw_lima_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# Santiago
def santiago_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        santiago.draw_santiago_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# Caracas
def caracas_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        caracas.draw_caracas_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# La Paz
def lapaz_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        lapaz.draw_caracas_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# La Paz
def asuncion_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        asuncion.draw_asun_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# Quito
def quito_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        quito.draw_ecuad_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# Montevideo
def mont_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        montevideo.draw_mont_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# Cusco
def cusco_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        cusco.draw_cusco_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# Manaus
def manaus_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        manaus.draw_manaus_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


# Bariloche
def barilo_screen():
    run = True
    while run:
        WIN.fill((0, 0, 0))
        bariloche.draw_barilo_window()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


main_menu()

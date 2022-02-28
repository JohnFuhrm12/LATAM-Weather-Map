import pygame
import os
pygame.font.init()

import requests
from bs4 import BeautifulSoup

# Scrape city weather info from Google using BeautifulSoup
city = "Brasilia"
url = "https://www.google.com/search?q=" + "weather" + city
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text

# Format Scraping Data
data = str.split('\n')
time = data[0]
sky = data[1]

# Text Fonts
CITY_FONT = pygame.font.SysFont('arial', 60)
TEMP_FONT = pygame.font.SysFont('arial', 40)
TIME_FONT = pygame.font.SysFont('arial', 45)
SKY_FONT = pygame.font.SysFont('arial', 45)

WIDTH, HEIGHT = 500, 700  # Game window dimensions
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Countries Flag
FLAG = pygame.transform.scale(pygame.image.load(
    os.path.join("Flags", "bra_flag.jpg")), (150, 100))

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join("Cities", "bra.jpg")), (WIDTH, HEIGHT))

def draw_bra_window():
    WIN.blit(BACKGROUND, (0, 0))
    city_text = CITY_FONT.render(
        (city), 1, BLACK)
    temp_text = TEMP_FONT.render(
        "Temperature: " + (temp), 1, BLACK)
    time_text = TIME_FONT.render(
        (time.capitalize()), 1, BLACK)
    sky_text = SKY_FONT.render(
        (sky.title()), 1, BLACK)

    WIN.blit(city_text, (20, 5))
    WIN.blit(temp_text, (20, 75))
    WIN.blit(time_text, (20, 125))
    WIN.blit(sky_text, (20, 180))
    WIN.blit(FLAG, (330, 20))
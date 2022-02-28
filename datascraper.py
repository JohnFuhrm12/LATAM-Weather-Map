import requests
from bs4 import BeautifulSoup

# Scrape city weather info from Google using BeautifulSoup
city = "Buenos Aires"
url = "https://www.google.com/search?q=" + "weather" + city
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text

# Format Data
data = str.split('\n')
time = data[0]
sky = data[1]

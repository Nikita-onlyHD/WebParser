from bs4 import BeautifulSoup
import requests
from requests import get
import time
import random

url = "https://osu.ppy.sh/rankings/osu/performance?page="
players = []
count = 1

try:
    pages = int(input('How many pages do you need(1 - 200): '))
except:
    print('Invalid value')
    exit()

if pages > 200 or pages < 1:
    print('Invalid value')
    exit()

print("Parsing from: https://osu.ppy.sh/rankings/osu/performance")

while count <= pages:
    url = "https://osu.ppy.sh/rankings/osu/performance?page=" + str(count)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    player_data = html_soup.find_all('tr', class_='ranking-page-table__row')
    if player_data != []:
        players.extend(player_data)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        time.sleep(scaled_value)
    else:
        print('empty')
        break

    print(f"Pages processed: {count}/{pages}")
    count += 1

print("Player in top: ", len(players))
print("-------------------------------------")

for player in players:
    top = player.find('td', {"class":"ranking-page-table__column ranking-page-table__column--rank"}).text.strip()
    name = player.find('a', {"class":"ranking-page-table__user-link-text js-usercard"}).text.strip()

    player_info = player.find_all('td', class_='ranking-page-table__column ranking-page-table__column--dimmed')
    acc = player_info[0].text.strip()
    play_count = player_info[1].text.strip()

    pp = player.find('td', {"class":"ranking-page-table__column ranking-page-table__column--focused"}).text.strip()
    print(top, name, '     Accuracy:', acc, '   Play count: ', play_count, '   pp:', pp)
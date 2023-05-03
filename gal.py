import requests
import csv
from bs4 import BeautifulSoup

def create_text():
  URL = 'https://www.chavesnamao.com.br/imoveis/pr-londrina/'
  page = requests.get(URL)

  soup = BeautifulSoup(page.content, "html.parser")

  card = soup.find_all("div", class_="imoveis__Card-obm8pe-0")
  house = []
  counter = 0

  for card in card:
    dadosExtra = card.find_all("li")
    if len(dadosExtra) > 1:
      adress = card.find("address")
      price = card.find("p", class_="price")
      kind = card.find("h2")
      size = dadosExtra[0]
      rooms = dadosExtra[1]

      house.append([])
      house[counter].append(adress.text.strip())
      house[counter].append(price.text.strip())
      house[counter].append(kind.text.strip())
      house[counter].append(size.text.strip())
      house[counter].append(rooms.text.strip())
      counter += 1

  return house

house_data = create_text()

with open('house_data.csv', mode='w', newline='') as file:

    writer = csv.writer(file)

    writer.writerow(['Address', 'Price', 'Kind', 'Size', 'Rooms'])

    for row in house_data:
        writer.writerow(row)
        
print("CSV file generated successfully.")
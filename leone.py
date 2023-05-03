# logradouro - string
# valor - string
# tipo do imovel - string
# tamanho - string
# tipo de contrato - string
# quartos - string

import requests
from bs4 import BeautifulSoup

URL = 'https://www.lopes.com.br/busca/venda/br/pr/londrina'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

imoveis = soup.find_all("div", class_="card ng-star-inserted")
print(imoveis)

imvs = []
for imovel in imoveis:
    kind = imovel.find("p", class_="card__type").text.strip()
    price = imovel.find("h4", class_="card__price ng-star-inserted").text.strip()
    price = 'R$\xa0390.000'
    price = price.replace('\xa0', ' ')
    adress = imovel.find("p", class_="card__location").text.strip()
    size = imovel.find_all("span", class_="attributes__info")[0].text.strip()
    rooms =  imovel.find_all("span", class_="attributes__info")[1].text.strip()
    if int(rooms) < 1:
        rooms = "Não há quartos"
    else:
        rooms += " Quartos"
        rooms = rooms.replace('0', '')

    imv = [adress, price, kind, size, rooms]
    imvs.append(imv)

print(imvs)

import csv

# Abre o arquivo CSV em modo de escrita "a"
with open('house_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    
    # Percorre a lista de imóveis e escreve cada item no arquivo CSV
    for imv in imvs:
        writer.writerow(imv)

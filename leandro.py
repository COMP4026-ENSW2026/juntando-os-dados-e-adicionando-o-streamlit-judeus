import requests
import csv
from bs4 import BeautifulSoup
import re

# URL = 'https://www.raulfulgencio.com.br/pesquisa-de-imoveis/?locacao_venda=L&id_cidade%5B%5D=1&finalidade=0&dormitorio=0&garagem=0&vmi=&vma='
URL = 'https://www.raulfulgencio.com.br/pesquisa-de-imoveis/?locacao_venda=L&id_cidade%5B%5D=1&id_tipo_imovel%5B%5D=4&id_tipo_imovel%5B%5D=6&id_tipo_imovel%5B%5D=8&id_tipo_imovel%5B%5D=10&id_tipo_imovel%5B%5D=57&id_tipo_imovel%5B%5D=13&id_tipo_imovel%5B%5D=12&finalidade=0&dormitorio=0&garagem=0&vmi=&vma='
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


# logradouro - string
# valor - string
# tipo do imovel - string
# tamanho - string
# quartos - string

cards = soup.find_all("div", class_="item col-sm-6 col-md-4 col-lg-3")
data_set = []
for card in cards:
    price = card.find("div", class_="price")
    price_value = price.find("span")
    # print(price_value.text.strip())
    info = card.find("div", class_="info")
    info_address = info.find("div", class_="amenities").find("a")
    info_type = info.find("div", class_="amenities").find("a").text
    rooms = info.find("ul",class_="imo-itens").find("li").text
    size = info.find("p",class_="corta_desc")
    # print(info_address['alt'])
    tamanho = ""
    padrao = r"(\d+)\s*m²"
    resultado = re.search(padrao, size.text)
    if resultado:
        tamanho = resultado.group(1) + " m²"

    data = [info_address['alt'].strip(), price_value.text.strip(), info_type.strip(), tamanho.strip(), rooms.strip()]
    data_set.append(data)

with open('house_data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    for data in data_set:
        writer.writerow(data)
    


    


import requests
from bs4 import BeautifulSoup
import csv
import streamlit as st
import pandas as pd

def generate_csv():
    URL = 'https://www.chavesnamao.com.br/imoveis/pr-londrina/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    card = soup.find_all("div", class_="imoveis__Card-obm8pe-0")
    house_data = []
    counter = 0

    for card in card:
        dadosExtra = card.find_all("li")
        if len(dadosExtra) > 1:
            adress = card.find("address")
            price = card.find("p", class_="price")
            kind = card.find("h2")
            size = dadosExtra[0]
            rooms = dadosExtra[1]

            house_data.append([])
            house_data[counter].append(adress.text.strip())
            house_data[counter].append(price.text.strip())
            house_data[counter].append(kind.text.strip())
            house_data[counter].append(size.text.strip())
            house_data[counter].append(rooms.text.strip())
            counter += 1

    with open('house_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Address', 'Price', 'Kind', 'Size', 'Rooms'])
        for row in house_data:
            writer.writerow(row)

    df = pd.read_csv("house_data.csv")
    st.write(df)



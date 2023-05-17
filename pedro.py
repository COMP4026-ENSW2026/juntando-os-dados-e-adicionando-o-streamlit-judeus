import requests
import csv
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import os
def generate_csv():
    URL = 'https://www.auroraimobi.com.br/imoveis/a-venda/londrina-pr?mobilia=talvez&condominio=&order=mais_relevantes'
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, "html.parser")
    dados_scraping = []
    for info in soup.find_all('div', {'class': 'ImovelCardInfo_info__QFwnz'}):
      kind =  info.find('span', {'class': 'text-primary'}).text.strip()
      ##nome = info.find('span', {'class': 'font-weight-bold'}).text.strip()
      address = info.find('div', {'class': 'col-11 p-0'}).find_all('p')[0].find_all('span', {'class': 'd-none'})[0].text.strip()+' '+ info.find('div', {'class': 'col-11 p-0'}).find_all('p')[0].find_all('span', {'class': 'd-none'})[1].text.strip() +' '+info.find('div', {'class': 'col-11 p-0'}).find_all('p')[1].text.strip()
      size = info.find('div', {'class': 'col-12 align-self-end'}).find_all('span')[0].text.strip()
      rooms = info.find('div', {'class': 'col-12 align-self-end'}).find_all('li')[1].text.strip()
      ##banheiros = info.find('div', {'class': 'col-12 align-self-end'}).find_all('li')[2].text.strip()
      ##contract = info.find('div', {'class': 'd-flex flex-column text-truncate'}).find_all('span')[0].text.strip()
      price = info.find('div', {'class': 'd-flex flex-column text-truncate'}).find_all('span')[1].text.strip()
      dados = [address, price, kind, size, rooms]
      dados_scraping.append(dados)
    nome_arquivo_csv = 'house_data.csv'
    
    # Abre o arquivo CSV em modo de escrita
    with open(nome_arquivo_csv, mode='a', newline='') as arquivo_csv:
        if(os.path.getsize(nome_arquivo_csv) == 0):
           writer = csv.writer(arquivo_csv, delimiter=',')
           writer.writerow(['Address', 'Price', 'Kind', 'Size', 'Rooms'])
           for data in dados_scraping:
              writer.writerow(data)
        else:    
            writer = csv.writer(arquivo_csv, delimiter=',')
            for data in dados_scraping:
               writer.writerow(data)

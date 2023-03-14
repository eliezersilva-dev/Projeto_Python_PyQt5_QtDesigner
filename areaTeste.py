"""
esse arquivo será deletado
"""
import json
import random
from datetime import date, datetime
import requests

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

headers = {
    'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
        'Safari/537.36 '
}

navegador.get('https://news.google.com/')


input(':')

# api cotações moedas
# cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
# cotacoes = cotacoes.json()
#
# dolar = str(cotacoes['USDBRL']['bid'])
# dolar = dolar.replace('.', ',')
# print('Dolar Americano')
# print(f'R$ {dolar}')
#
# euro = str(cotacoes['EURBRL']['bid'])
# euro = euro.replace('.', ',')
# print('Euro')
# print(f'R$ {euro}')
#
# btc = str(cotacoes['BTCBRL']['bid'])
# print('Bitcoin')
# print(f'{btc} mil reais')


# api previsão do tempo
# consulta = input('Capital: ')
# with open('arquivos/previsoes_capitais_brasil.txt', 'r', encoding="utf8") as arquivo_previsoes:
#     capitais = arquivo_previsoes.read()
#     capitais = json.loads(capitais)
#     with open('arquivos/capitais_estados.txt', 'r', encoding="utf8") as arquivo_capitais:
#         estados = arquivo_capitais.read()
#         estados = json.loads(estados)
#         for i, j in estados.items():
#             if consulta in i:
#                 estado = j
#                 print(f'{consulta}/{estado}')
#
#     consulta = capitais[consulta]
#
# previsao = requests.get(consulta)
# previsao = previsao.json()
#
# # dia
# data = previsao['daily']
# data = data['time']
# data = data[0]
# data = datetime.strptime(data, '%Y-%m-%d').date()
# data = datetime.strftime(data, '%d/%m/%Y')
# print(f'Data: {data}')
#
# # temperatura mínima
# temp_min = previsao['daily']
# temp_min = temp_min['temperature_2m_min']
# temp_min = temp_min[0]
# print(f'Temperatura Mínima: {temp_min}')
#
# # temperatura máxima
# temp_max = previsao['daily']
# temp_max = temp_max['temperature_2m_max']
# temp_max = temp_max[0]
# print(f'Temperatura Máxima: {temp_max}')
#
# # precipitação
# precipitacao = previsao['daily']
# precipitacao = precipitacao['precipitation_sum']
# precipitacao = precipitacao[0]
# print(f'Precipitação de chuva última hora: {precipitacao} mm')


# arquivo proverbios
# with open('arquivos/proverbios.txt', 'r', encoding="utf8") as arquivo:
#     proverbios = arquivo.readlines()
#     print(random.choice(proverbios))





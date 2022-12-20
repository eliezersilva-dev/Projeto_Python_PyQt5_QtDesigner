"""
esse arquivo será deletado
"""
import json
import random
from datetime import date, datetime
import requests




# api GoogleNews - pip install GoogleNews
# from GoogleNews import GoogleNews
# noticias = GoogleNews(period='d')
# noticias.setlang('pt')
# noticias.search('petroleo')
# resultado = noticias.results()
# print(resultado)
# noticia1 = resultado[0]
# print(noticia1['desc'])
# print(noticia1['link'])
# noticia1 = resultado[1]
# print(noticia1['desc'])
# print(noticia1['link'])



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
consulta = input('Capital: ')
with open('arquivos/previsoes_capitais_brasil.txt', 'r', encoding="utf8") as arquivo_previsoes:
    capitais = arquivo_previsoes.read()
    capitais = json.loads(capitais)
    with open('arquivos/capitais_estados.txt', 'r', encoding="utf8") as arquivo_capitais:
        estados = arquivo_capitais.read()
        estados = json.loads(estados)
        for i, j in estados.items():
            if consulta in i:
                estado = j
                print(f'{consulta}/{estado}')

    consulta = capitais[consulta]

previsao = requests.get(consulta)
previsao = previsao.json()

# dia
data = previsao['daily']
data = data['time']
data = data[0]
data = datetime.strptime(data, '%Y-%m-%d').date()
data = datetime.strftime(data, '%d/%m/%Y')
print(f'Data: {data}')

# temperatura mínima
temp_min = previsao['daily']
temp_min = temp_min['temperature_2m_min']
temp_min = temp_min[0]
print(f'Temperatura Mínima: {temp_min}')

# temperatura máxima
temp_max = previsao['daily']
temp_max = temp_max['temperature_2m_max']
temp_max = temp_max[0]
print(f'Temperatura Máxima: {temp_max}')

# precipitação
precipitacao = previsao['daily']
precipitacao = precipitacao['precipitation_sum']
precipitacao = precipitacao[0]
print(f'Precipitação de chuva última hora: {precipitacao} mm')



# arquivo proverbios
# with open('arquivos/proverbios.txt', 'r', encoding="utf8") as arquivo:
#     proverbios = arquivo.readlines()
#     print(random.choice(proverbios))



